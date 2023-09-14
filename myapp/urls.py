from django.urls import path
from .views import index
from .views import homePageView
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView 
urlpatterns = [
    path('', index, name='index'),
    
    path('robots.txt',TemplateView.as_view(template_name="main/robots.txt", content_type="text/plain")),  #add the robots.txt file

    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
