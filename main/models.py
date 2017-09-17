from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                    self).get_queryset().filter(status='published')

class News(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    CATEGORY_CHOICES = (
        ('news', 'News'),
        ('product', 'Product'),
        ('employment', 'Employment'),
    )
    category = models.CharField(max_length=10,
                                choices=CATEGORY_CHOICES,
                                default='news')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='news_posts')
    intro = models.TextField(default='请编剧简介')
    body = RichTextUploadingField(default='请编辑内容')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        ordering = ('-publish',)
        verbose_name_plural = 'Content'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:news_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])