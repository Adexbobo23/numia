from django.urls import path
from .views import (
    home, about, booking, contact,
    menu, service, team, testimonial
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('booking/', booking, name='booking'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('menu/', menu, name='menu'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
]