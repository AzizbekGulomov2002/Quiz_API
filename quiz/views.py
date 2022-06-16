# from django.shortcuts import render

# from ckeditor.fields import RichTextField
# from .models import *
# def getsavol(request):
#     savollar = SavolBody.objects.all()
#     # 40 tasini  o'qib olish
#     # aralashtirish 
#     return render(request, "index.html", {"savollar":savollar})

from rest_framework.viewsets import ModelViewSet
from .serializers import SavolBodySerializer, FanlarSerializer, SavolDarajasiSerializer
from .models import SavolDarajasi, SavolBody, Fanlar


class FanlarViewSet(ModelViewSet):
    queryset = Fanlar.objects.all()
    serializer_class = FanlarSerializer
    http_method_names = ['get', 'head']


# class SavolBodyViewSet(ModelViewSet):
#     queryset = SavolBody.objects.all()
#     serializer_class = SavolBodySerializer
#     http_method_names = ['get', 'head']

class SavolBodyViewSet(ModelViewSet):
    queryset = SavolBody.objects.all()
    serializer_class = SavolBodySerializer
    http_method_names = ['get', 'head']
    
    def get_queryset(self):
        queryset = SavolBody.objects.all()
        n = self.request.query_params.get('random', None)
        if n is not None:
            n = int(n)
            queryset = queryset.order_by('?')[:n]
       
        return queryset
    


class SavolDarajasiViewSet(ModelViewSet):
    queryset = SavolDarajasi.objects.all()
    serializer_class = SavolDarajasiSerializer
    http_method_names = ['get', 'head']
    

