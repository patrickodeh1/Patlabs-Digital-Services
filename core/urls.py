from django.urls import path
from .views import HomePageView, AboutPageView, ServicesPageView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', views.contact_us, name='contact'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('get-quote/', views.get_quote, name='get_quote'),
]