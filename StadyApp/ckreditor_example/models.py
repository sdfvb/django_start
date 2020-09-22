from datetime import datetime

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class PostCKEditor(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    # description = RichTextField(blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    slug = models.SlugField(default='', blank=True)

    def save(self):
        date = datetime.now()
        self.slug = '%i_%i_%i_%i_%i_%i_%s' % (
            date.year, date.month, date.day, date.hour, date.minute, date.second, slugify(self.title))
        super(PostCKEditor, self).save()

    def get_absolute_url(self):
        """генерирует ссылку вместо {% url 'post_detail_url' slug=post.slug%}"""
        return reverse('post_detail_ckeditor', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
