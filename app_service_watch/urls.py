from django.contrib import admin
from django.urls import path
from .views import *
from app_service_watch import views

urlpatterns = [
    path("", index, name="Inicio"),
    path("clients/", clients, name="Clientes"),
    path("clients_form/", clients_form, name="ClientsForm"),
    path("staff/", staff, name="Staff"),
    path("staff_form/", staff_form, name="StaffForm"),
    path("services_provided/", services_provided, name="Servicios Prestados"),
    path("services_provided_form/", services_provided_form, name="ServProvForm"),
    path("pending_services/", pending_services, name="Servicios Pendientes"),
    path("pending_services_form/", pending_services_form, name="PendServForm"),
    path("search/", search, name="Search Bar"),
    path("about/", about, name="About")
]

urlpatterns += [
    path("clients/list/", views.ClientListView.as_view(), name="Lista de Clientes"),
    path("clients/detail/<int:pk>/", views.ClientDetailView.as_view(), name="Detalle de Cliente"),
    path("clients/create/", views.ClientCreateView.as_view(), name="Crear Cliente"),
    path("clients/update/<int:pk>/", views.ClientUpdateView.as_view(), name="Actualizar Cliente"),
    path("clients/delete/<int:pk>/", views.ClientDeleteView.as_view(), name="Borrar Cliente"),
    path("staff/list/", views.StaffListView.as_view(), name="Lista de Staff"),
    path("staff/detail/<int:pk>/", views.StaffDetailView.as_view(), name="Detalle de Staff"),
    path("staff/create/", views.StaffCreateView.as_view(), name="Crear Staff"),
    path("staff/update/<int:pk>/", views.StaffUpdateView.as_view(), name="Actualizar Staff"),
    path("staff/delete/<int:pk>/", views.StaffDeleteView.as_view(), name="Borrar Staff"),
    path("pending_services/list/", views.PendingServicesListView.as_view(), name="Lista de Servicios en Curso"),
    path("pending_services/detail/<int:pk>/", views.PendingServicesDetailView.as_view(), name="Detalle de Servicios en Curso"),
    path("pending_services/create/", views.PendingServicesCreateView.as_view(), name="Crear Servicios en Curso"),
    path("pending_services/update/<int:pk>/", views.PendingServicesUpdateView.as_view(), name="Actualizar Servicios en Curso"),
    path("pending_services/delete/<int:pk>/", views.PendingServicesDeleteView.as_view(), name="Borrar Servicios en Curso"),
    path("services_provided/list/", views.ServicesProvidedListView.as_view(), name="Lista de Servicios Prestados"),
    path("services_provided/detail/<int:pk>/", views.ServicesProvidedDetailView.as_view(), name="Detalle de Servicios Prestados"),
    path("services_provided/create/", views.ServicesProvidedCreateView.as_view(), name="Crear Servicios Prestados"),
    path("services_provided/update/<int:pk>/", views.ServicesProvidedUpdateView.as_view(), name="Actualizar Servicios Prestados"),
    path("services_provided/delete/<int:pk>/", views.ServicesProvidedDeleteView.as_view(), name="Borrar Servicios Prestados"),
]

