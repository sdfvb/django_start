# Generated by Django 3.1.1 on 2020-09-18 09:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ckreditor_example', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postckeditor',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
