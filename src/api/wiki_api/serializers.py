from wiki_api.models import WikiUser, Domain, Page, Group
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist


class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_representation(self, value):
        try:
            return super(CreatableSlugRelatedField, self).to_representation(value)
        except:
            return str(value)
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=str(data))
        except (TypeError, ValueError):
            self.fail('invalid')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['group_name']

class DomainSerializer(serializers.HyperlinkedModelSerializer):
    page_count = serializers.SerializerMethodField()
    class Meta:
        model = Domain
        fields = ['domain_name', 'page_count']


    def get_page_count(self, obj):
        return obj.page_set.count()

class PageListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        pages = []
        for item in validated_data:
            page_author = item.pop('page_author')
            page_domain = item.pop('page_domain')
            domain, created = Domain.objects.get_or_create(
                domain_name=page_domain)

            wiki_users = WikiUser.objects.filter(
                wiki_user_id=page_author["wiki_user_id"])

            if wiki_users.count() > 0:
                wiki_user = wiki_users[0]
            else:
                wiki_user_groups = page_author.pop('wiki_user_groups')

                wiki_user = WikiUser.objects.create(**page_author)

                for user_group in wiki_user_groups:
                    gr, cr = Group.objects.get_or_create(
                        group_name=user_group)
                    wiki_user.wiki_user_groups.add(user_group)

            pages.append(Page(page_author=wiki_user,page_domain=page_domain,
                                                       **item))

        return Page.objects.bulk_create(pages)



class WikiUserSerializer(serializers.HyperlinkedModelSerializer):
    wiki_user_groups = CreatableSlugRelatedField(
        read_only=False,
        slug_field='group_name',
        queryset=Group.objects.all(),
        many=True
     )
    page_count = serializers.SerializerMethodField()
    class Meta:
        model = WikiUser
        fields = ['wiki_user_id', 'wiki_user_text', 'wiki_user_groups',
                  'wiki_user_is_bot', 'wiki_user_registration_dt',
                  'page_count'
                  ]
        extra_kwargs = {
            'wiki_user_id': {
                'validators': [],
            }
        }


    def get_page_count(self, obj):
        if type(obj) == dict:
            return 0
        else:
            return obj.page_set.count()

    def create(self, validated_data):
        wiki_user_groups = validated_data.pop('wiki_user_groups')
        groups = []
        for wiki_user_group in wiki_user_groups:
            group, created = Domain.objects.get_or_create(
                group_name=wiki_user_group)
            groups.append(group)
        wiki_user = WikiUser.objects.get_or_create(wiki_user_groups=groups,**validated_data)
        return wiki_user

class PageSerializer(serializers.HyperlinkedModelSerializer):
    page_domain = CreatableSlugRelatedField(
        read_only=False,
        slug_field='domain_name',
        queryset=Domain.objects.all()
     )
    page_author = WikiUserSerializer()
    class Meta:
        model = Page
        list_serializer_class = PageListSerializer
        fields = ['page_uri', 'page_wiki_id', 'page_domain', 'page_wiki_id_num',
                  'page_title', 'page_creation_timestamp', 'page_author']

    def create(self, validated_data):

        page_author = validated_data.pop('page_author')
        page_domain = validated_data.pop('page_domain')
        domain, created  = Domain.objects.get_or_create(domain_name=page_domain)

        wiki_users = WikiUser.objects.filter(wiki_user_id=page_author["wiki_user_id"])

        if wiki_users.count()>0:
            wiki_user = wiki_users[0]
        else:
            wiki_user_groups = page_author.pop('wiki_user_groups')

            wiki_user = WikiUser.objects.create(**page_author)

            for user_group in wiki_user_groups:
                gr, cr = Group.objects.get_or_create(group_name=user_group)
                wiki_user.wiki_user_groups.add(user_group)

        page,created = Page.objects.get_or_create(page_author=wiki_user,
                                   page_domain=page_domain,**validated_data)

        return page

