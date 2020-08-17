from time import time

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def gen_slug(some_text):
    new_slug = slugify(some_text, allow_unicode=True)
    return f'{new_slug}-{str(int(time()))}'


class Post(models.Model):
    """ Data_Base Table """
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    # Связь с таблицой Tag
    # Post.tags = Tag.posts
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    class Meta:
        # критерии сортировки
        ordering = ['-date_pub']

    def get_absolute_url(self):
        """генерирует ссылку вместо {% url 'post_detail_url' slug=post.slug%}"""
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # id появляется при записи первый раз в БД
        if not self.id:
            self.slug = gen_slug(self.title)

        super().save(*args, **kwargs)

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    # posts от Post

    class Meta:
        # критерии сортировки
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})