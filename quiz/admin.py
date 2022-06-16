from django.contrib import admin
from .models import SavolBody,SavolDarajasi, Fanlar
# Register your models here.
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
# class PostAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = SavolBody

# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForm

# admin.site.register(SavolBody, PostAdmin)
admin.site.register(SavolDarajasi)
@admin.register(SavolBody)
class SavolTanasi(admin.ModelAdmin):
    list_display = ['level','subject']
    list_per_page = 10
    ordering = ('subject','level')

@admin.register(Fanlar)
class FanTanasi(admin.ModelAdmin):
    list_display = ['id','fan']
    # list_per_page = 10
