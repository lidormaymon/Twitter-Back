# Generated by Django 4.2.2 on 2023-09-04 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_tweets_edit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
