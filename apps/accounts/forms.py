from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs['class']='form__field'

    class Meta:
        model=Articulo
        exclude=['codigo_de_barras']
        labels={
            'img':'Imagen',
            'dec':'Descripción',
        }
