# Generated by Django 4.0.4 on 2022-05-13 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_link', models.CharField(max_length=500)),
                ('slug_data', models.CharField(max_length=10)),
            ],
        ),
    ]
