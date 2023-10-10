from django.urls import path
from .views import index
from .views import homePageView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import MySitemap


from django.views.generic.base import TemplateView 

sitemaps = {
    'mysitemap': MySitemap,
}

urlpatterns = [
    path('', index, name='index'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),    
    path('robots.txt',TemplateView.as_view(template_name="main/robots.txt", content_type="text/plain")),  #add the robots.txt file

    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
