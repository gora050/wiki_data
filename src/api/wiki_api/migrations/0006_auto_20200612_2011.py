# Generated by Django 3.0.7 on 2020-06-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki_api', '0005_auto_20200612_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikiuser',
            name='wiki_user_registration_dt',
            field=models.DateTimeField(null=True),
        ),
    ]
