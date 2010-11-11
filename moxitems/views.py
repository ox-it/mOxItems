import django.contrib.syndication.views 
from moxitems.models import Feed, Items

# Create your views here.

class TestFeed(django.contrib.syndication.views.Feed):
    
    def get_object(self, request, slug):
        return get_object_or_404(Feed, slug=slug)
    
    def items(self, feed):
        return Item.objects.filter(feed=feed)
        
    def title(self, feed):
        return feed.title
        
    def description(self, feed):
        return feed.description
        
    def link(self, feed):
        return feed.link
    
    # Items
    
