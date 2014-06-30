from django.contrib import admin
from blog.models import Entry


class EntryAdmin(admin.ModelAdmin):
    fields = ['title', 'published' ,'body']
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Entry, EntryAdmin)
