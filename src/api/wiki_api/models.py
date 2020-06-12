from django.db import models

# Create your models here.


class Domain(models.Model):
    domain_name = models.CharField(max_length=250, unique=True)

class Group(models.Model):
    group_name = models.CharField(max_length=64, unique=True)


class Page(models.Model):
    page_uri = models.CharField(max_length=500)
    page_wiki_id = models.CharField(max_length=64,unique=True)
    page_domain = models.ForeignKey('Domain', on_delete=models.CASCADE,)
    page_wiki_id_num = models.IntegerField(unique=True)
    page_title = models.CharField(max_length=250)
    page_creation_timestamp = models.DateTimeField()
    page_author = models.ForeignKey('WikiUser', on_delete=models.CASCADE,
                                    null=True)

class WikiUser(models.Model):
    wiki_user_id = models.CharField(max_length=32, unique=True)
    wiki_user_text = models.CharField(max_length=32)
    wiki_user_groups = models.ManyToManyField(Group, blank=True)
    wiki_user_is_bot = models.BooleanField(default=False)
    wiki_user_registration_dt = models.DateTimeField()
    