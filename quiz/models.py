from tabnanny import verbose
from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

class SavolDarajasi(models.Model):
    daraja = models.CharField(max_length=200)
    def __str__(self):
        return self.daraja
    
    class Meta:
        verbose_name = 'Savol darajasi'
        verbose_name_plural = 'Savol darajalari'

class Fanlar(models.Model):
    fan = models.CharField(max_length=200)
    def __str__(self):
        return self.fan
    
    class Meta:
        verbose_name = 'Fan'
        verbose_name_plural = 'Fanlar'
        

class SavolBody(models.Model):
    subject = models.ForeignKey(Fanlar, on_delete=models.CASCADE)
    level = models.ForeignKey(SavolDarajasi, on_delete=models.CASCADE, default="1")
    savol = RichTextField(config_name='savol_awesome_ckeditor')
    correct_answer = RichTextField(config_name='awesome_ckeditor')
    error_answer_1 = RichTextField(config_name='awesome_ckeditor')
    error_answer_2 = RichTextField(config_name='awesome_ckeditor')
    error_answer_3 = RichTextField(config_name='awesome_ckeditor')
    
    
    class Meta:
        verbose_name = 'Test savol'
        verbose_name_plural = 'Test savollari'