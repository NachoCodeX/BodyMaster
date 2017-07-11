from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _

class ProductForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs['class']='form__field'

    class Meta:
        model=Articulo
        exclude=['codigo_de_barras','img']
        labels={
            'img':'Imagen',
            'dec':'Descripción',
        }


class ProductUpdateForm(forms.ModelForm):
    # img=forms.ImageField(label=_('Imagen'),required=False,widget=forms.FileInput)
    def __init__(self,*args,**kwargs):
        super(ProductUpdateForm,self).__init__(*args,**kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs['class']='form__field'
        # self.fields['img'].widget.attrs['class']='form__field form__field--img'
        # self.fields['img'].widget.attrs['id']='upload'

    class Meta:
        model=Articulo
        exclude=['codigo_de_barras','img']
        labels={
            'img':'Imagen',
            'dec':'Descripción',
        }
