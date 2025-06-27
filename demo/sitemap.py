from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return [
            'home:home',
            'home:about',
            'home:contact',
            'home:gallery',
            'home:register',
            'home:courses',
            'home:activity',
        ]

    def location(self, item):
        return reverse(item)


