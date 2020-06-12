from django.shortcuts import render
from django_filters import rest_framework as filters

from wiki_api.models import WikiUser, Domain, Page
from rest_framework import viewsets
from wiki_api.serializers import (DomainSerializer, PageSerializer,
        WikiUserSerializer)


class DomainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows domains to be viewed or edited.
    """
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows wiki pages to be viewed or edited.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = {
    'page_wiki_id' : ['exact'],
    'page_domain__domain_name' : ['exact'],
    'page_wiki_id_num' : ['exact'],
    'page_title' : ['exact'],
    'page_creation_timestamp' : ['gte', 'lt', 'exact'],
    'page_author__wiki_user_id' : ['exact']}

    search_fields = ('page_wiki_id')
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            if isinstance(data, list):
                kwargs["many"] = True

        return super(PageViewSet, self).get_serializer(*args, **kwargs)

class WikiUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows wiki users to be viewed or edited.
    """
    queryset = WikiUser.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = {
        'page__page_creation_timestamp': ['gte', 'lt'],
    }
    serializer_class = WikiUserSerializer
