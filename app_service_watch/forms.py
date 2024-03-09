from django import forms
 
class ClientsForm(forms.Form):
    name = forms.CharField(max_length=40, label="Nombre")
    last_name = forms.CharField(max_length=30, label="Apellido")
    email = forms.EmailField(max_length=40, label="Email")
    company = forms.CharField(max_length=30, label="Empresa")

class StaffForm(forms.Form):
    name = forms.CharField(max_length=40, label="Nombre")
    last_name = forms.CharField(max_length=30, label="Apellido")
    email = forms.EmailField(max_length=40, label="Email")

class ServicesProvidedForm(forms.Form):
    name = forms.CharField(max_length=60, label="Nombre")
    completion_date = forms.DateField(label="Completado el día")
    completed = forms.BooleanField(label="Entregado")

class PendingServicesForm(forms.Form):
    name = forms.CharField(max_length=60, label="Nombre")
    status_update_date = forms.DateField(label="Actualizado el día")
    status = forms.CharField(max_length=20, label="Estado")

class Search(forms.Form):
    name = forms.CharField(max_length=60, label="Nombre")