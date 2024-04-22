from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactApiView.as_view(), name='index'),
    # Other URL patterns...
]
