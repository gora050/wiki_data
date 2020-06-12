# Generated by Django 3.0.7 on 2020-06-12 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki_api', '0006_auto_20200612_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_wiki_id',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='wikiuser',
            name='wiki_user_id',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='wikiuser',
            name='wiki_user_text',
            field=models.CharField(max_length=250),
        ),
    ]
