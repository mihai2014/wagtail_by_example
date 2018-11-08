# Generated by Django 2.1.2 on 2018-11-05 20:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailmenus', '0022_auto_20170913_2125'),
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AppIndexPage',
            new_name='AppPage',
        ),
    ]
