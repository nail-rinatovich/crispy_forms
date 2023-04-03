from django.urls import path
from .views import index
from .views import homePageView
urlpatterns = [
    path('', index, name='index'),
    # path('', homePageView, name='home'),
]
