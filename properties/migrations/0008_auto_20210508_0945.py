# Generated by Django 3.0.8 on 2021-05-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_auto_20210504_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properttype',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
