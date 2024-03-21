from django import forms

class TimeInput(forms.TimeInput):
    input_type = 'time'

class CreateNewIngreso(forms.Form):
    horaIngreso = forms.TimeField(label="Hora de ingreso", widget=TimeInput)

class ModifyIngreso(forms.Form):
    nro = forms.IntegerField(label="Número de Ingreso",widget=forms.NumberInput)
    horaSalida = forms.IntegerField(label="Hora de salida", widget=TimeInput)
