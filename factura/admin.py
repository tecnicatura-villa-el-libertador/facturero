from django.contrib import admin
from django import forms
# Register your models here.
from .models import Factura, Cliente, Renglon, Articulo
import autocomplete_light

class RenglonForm(forms.ModelForm):
    articulo = forms.ModelChoiceField(Articulo.objects.all(),
                                      widget=autocomplete_light.ChoiceWidget('ArticuloAutocomplete'))

    class Meta:
        model = Renglon
        fields = ['cantidad', 'articulo', 'total']


class RenglonInline(admin.TabularInline):
    form = RenglonForm
    model = Renglon


class FacturaAdmin(admin.ModelAdmin):
    inlines = [
        RenglonInline
    ]

admin.site.register(Factura, FacturaAdmin)
admin.site.register(Cliente)
admin.site.register(Renglon)
admin.site.register(Articulo)
