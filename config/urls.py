from django.contrib import admin
from django.urls import path, include

from markdown.views import frontpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",frontpage),
    path("mdeditor", include('mdeditor.urls'))
]