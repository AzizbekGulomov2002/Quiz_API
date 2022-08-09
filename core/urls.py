
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from quiz.views import getsavol
from django.views.static import serve
from django.conf.urls import url
from django.urls import reverse
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^ckeditor/', include('ckeditor.urls')),
]
urlpatterns+=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)