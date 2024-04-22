from django.contrib import admin
from django.urls import path, include

from contact.views import ContactApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/contactlist/', ContactApiView.as_view()),
    path('', include('contact.urls')),
]
