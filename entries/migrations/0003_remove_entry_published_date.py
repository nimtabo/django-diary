# Generated by Django 2.2.2 on 2019-06-23 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_entry_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='published_date',
        ),
    ]
