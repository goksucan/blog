# Generated by Django 3.2.5 on 2022-07-17 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20220717_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thunbnail',
            new_name='thumbnail',
        ),
    ]
