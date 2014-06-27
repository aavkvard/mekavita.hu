from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=64)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    published = models.BooleanField()
    author = models.ForeignKey(User)
    body = models.TextField()
 
    def __str__(self):
        return "%s (%s)" % (self.title, self.author.name)

