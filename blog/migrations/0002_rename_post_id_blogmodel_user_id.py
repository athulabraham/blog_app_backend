# Generated by Django 4.1.2 on 2023-11-17 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogmodel',
            old_name='post_id',
            new_name='user_id',
        ),
    ]
