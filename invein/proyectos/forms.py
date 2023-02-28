from django import forms
from .models import Comercial, Cliente, Proyecto, Fabricacion, Montaje, Oferta, Actividad, Comentarios, CurvaS


class ComercialForm(forms.ModelForm):
    class Meta:
        model = Comercial
        exclude = ['uc', 'um', 'creado', 'actualizado']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['uc', 'um', 'creado', 'actualizado']


class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        exclude = ['uc', 'um', 'creado', 'actualizado']


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        exclude = ['uc', 'um', 'creado', 'actualizado']
        widgets = {
            'fecha_inicio':forms.DateInput(attrs={'placeholder':'dd/mm/aaaa'}),
            'fecha_fin':forms.DateInput(attrs={'placeholder':'dd/mm/aaaa'})
        }

class FabricacionForm(forms.ModelForm):
    class Meta:
        model = Fabricacion
        exclude = ['uc', 'um', 'creado', 'actualizado']


class MontajeForm(forms.ModelForm):
    class Meta:
        model = Montaje
        exclude = ['uc', 'um', 'creado', 'actualizado']

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        exclude = ['uc', 'um', 'creado', 'actualizado']
        widgets = {
            'fecha_inicio':forms.DateInput(attrs={'placeholder':'dd/mm/aaaa'}),
            'fecha_fin':forms.DateInput(attrs={'placeholder':'dd/mm/aaaa'})
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['comentarios']

class CurvaForm(forms.ModelForm):
    class Meta:
        model = CurvaS
        fields = ['fecha', 'programado', 'avance']