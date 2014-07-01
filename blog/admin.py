from django.contrib import admin
from blog.models import Entry
#from django_summernote.admin import SummernoteModelAdmin

#class EntryAdmin(SummernoteModelAdmin):
class EntryAdmin(admin.ModelAdmin):
    fields = ['title', 'published' ,'body']
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
	    '/static/blog/tinymce_setup.js',
        ]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Entry, EntryAdmin)
