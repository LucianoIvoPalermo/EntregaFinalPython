from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=40, verbose_name="Nombre")
    last_name = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.EmailField(max_length=40, verbose_name="Email")
    company = models.CharField(max_length=30, verbose_name="Empresa")

    def __str__(self):
        return f"Nombre: {self.name} / Apellido: {self.last_name} / Email: {self.email} / Compañía: {self.company}"    

class Staff(models.Model):
    name = models.CharField(max_length=40, verbose_name="Nombre")
    last_name = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.EmailField(max_length=40, verbose_name="Email")

    def __str__(self):
        return f"Nombre: {self.name} / Apellido: {self.last_name} / Email: {self.email}"

class ServicesProvided(models.Model):
    name = models.CharField(max_length=60, verbose_name="Descripción")
    completion_date = models.DateField(verbose_name="Fecha de finalización")
    completed = models.BooleanField(verbose_name= "Entregado", null=True, blank=True)

    def __str__(self):
        return f"Servicio brindado: {self.name} / Completado el: {self.completion_date} / Entregado: {self.completed}"

class PendingServices(models.Model):
    name = models.CharField(max_length=60, verbose_name="Descripción")
    status_update_date = models.DateField(verbose_name="Fecha de actualización")
    status = models.CharField(max_length=20, verbose_name="Estado")

    def __str__(self):
        return f"Servicio Pendiente: {self.name} / Actualizado: {self.status_update_date} / Estado: {self.status}"
