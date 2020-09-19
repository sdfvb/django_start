from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.utils.text import slugify


class PostCKEditor(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    # description = RichTextField(blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(default='', blank=True)

    def save(self):
        self.slug = slugify(self.title)
        super(PostCKEditor, self).save()

    def __str__(self):
        return self.title
