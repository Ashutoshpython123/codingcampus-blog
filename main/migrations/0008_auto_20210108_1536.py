# Generated by Django 3.1.3 on 2021-01-08 10:06

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210108_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_content',
            field=tinymce.models.HTMLField(),
        ),
    ]
