from django.contrib import admin
from blog.models import Entry


class EntryAdmin(admin.ModelAdmin):
    fields = ['title', 'published' ,'body']

admin.site.register(Entry, EntryAdmin)
