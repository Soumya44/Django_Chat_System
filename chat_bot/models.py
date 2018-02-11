from django.db import models
from django.core.urlresolvers import reverse


class Message(models.Model):
    title = models.CharField(max_length=255, default="User")
    slug = models.SlugField(max_length=255, unique=False, blank=True, default="msg")
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ['created']

        def __unicode__(self):
            return u'%s'%self.title
