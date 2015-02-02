from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from blog.models import Entry

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_entries'

    def get_queryset(self):
        return Entry.objects.filter(published__exact=True).order_by('-modified')[:10]


class EntryView(generic.DetailView):
    model = Entry
    template_name = 'blog/entry.html'

def index(request):
    latest_entries = Entry.objects.all().order_by('-pub_date')[:5]
    context = {'latest_entries': latest_entries}
    return render(request, 'blog/index.html', context)
