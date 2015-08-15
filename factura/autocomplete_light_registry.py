import autocomplete_light
from .models import Articulo


class ArticuloAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['descripcion', 'codigo_barra', 'id']


autocomplete_light.register(Articulo,
                            ArticuloAutocomplete,
                            name='ArticuloAutocomplete',
                            choices=Articulo.objects.all())
