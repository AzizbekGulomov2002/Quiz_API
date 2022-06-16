
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
# from quiz.views import getsavol

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls')),
]
