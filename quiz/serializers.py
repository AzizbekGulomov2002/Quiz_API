from rest_framework import serializers
from .models import SavolDarajasi, Fanlar, SavolBody


class SavolDarajasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavolDarajasi
        fields = '__all__'


class FanlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fanlar
        fields = '__all__'
        




class SavolBodySerializer(serializers.ModelSerializer):
    subject = FanlarSerializer()
    level = SavolDarajasiSerializer()
    class Meta:
        model = SavolBody
        fields = '__all__'