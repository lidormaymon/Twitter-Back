# Generated by Django 4.2.2 on 2023-09-11 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_rename_content_message_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]