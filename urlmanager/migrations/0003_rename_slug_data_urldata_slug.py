# Generated by Django 4.0.4 on 2022-05-13 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlmanager', '0002_rename_big_link_urldata_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urldata',
            old_name='slug_data',
            new_name='slug',
        ),
    ]
