from django import forms 
from .models import Producto

class ProductosForm(forms.ModelForm):
    class Meta:
      model = Producto
      fields = "__all__"
    
