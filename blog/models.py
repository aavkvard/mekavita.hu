from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField()
    author = models.ForeignKey(User)
    body = models.TextField()

    class Meta:
        verbose_name_plural = "entries"
 
    def __str__(self):
        return "%s (%s)" % (self.title, self.author.username)

