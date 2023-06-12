from django.contrib import admin
from django.urls import path

from markdown.views import frontpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",frontpage)
]
