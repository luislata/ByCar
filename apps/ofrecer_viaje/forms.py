from django import forms

from apps.ofrecer_viaje.models import ofrecer_viaje

class ofrecerviajeForm(forms.ModelForm):

    class Meta:
        model = ofrecer_viaje

        fields = [
            'nombre',
            'telefono_contacto',
            'lugar_de_partida',
            'destino',
            'fecha',
            'hora',
            'asientos_disponibles',
            'costo',
        ]


        labels = {
            'nombre' :'Nombre',
            'telefono_contacto' : 'Telefono_contacto',
            'lugar_de_partida' : 'Lugar_de_partida',
            'destino' : 'destino',
            'fecha' : 'Fecha',
            'hora' : 'Hora',
            'asientos_disponibles' : 'Asientos_disponibles',
            'costo' : 'Costo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'lugar_de_partida': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'hora': forms.TextInput(attrs={'class': 'form-control'}),
            'asientos_disponibles': forms.TextInput(attrs={'class': 'form-control'}),
            'costo': forms.TextInput(attrs={'class': 'form-control'}),
        }
