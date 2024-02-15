from django.db import models

# Create your models here.
from django.shortcuts import reverse


# Create your models here.
class Comp(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    name = models.TextField(max_length=150, db_index=True)
    type = models.TextField(max_length=150, db_index=True)
    halal = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('comp_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('comp_tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)
