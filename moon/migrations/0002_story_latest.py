# Generated by Django 4.1.4 on 2022-12-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='latest',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
