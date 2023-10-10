from django.contrib import sitemaps
from django.urls import reverse

class MySitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        # Верните объекты, которые вы хотите включить в карту сайта
        return ['index']

    def location(self, item):
        # Определите URL-адрес для каждого элемента
        return reverse(item)
