from django.shortcuts import render
from app_service_watch.models import *
from app_service_watch.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from users.models import Avatar

def index(request):
    try:
        avatares = Avatar.objects.get(user__id=request.user.id)
        imagen = avatares.imagen.url
    except:
        imagen = ""

    return render (request, "app_service_watch/index.html", {"url": imagen} )

class ClientListView(LoginRequiredMixin, ListView):
    model = Clients
    template_name = "app_service_watch/client_list.html"

class ClientDetailView (LoginRequiredMixin, DetailView):
    model = Clients
    template_name = "app_service_watch/client_detail.html"

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Clients
    template_name = "app_service_watch/client_create.html"
    fields = ['name', 'last_name', 'email', 'company']
    success_url = reverse_lazy('Lista de Clientes')
    
    def form_valid(self, form):
        messages.success(self.request, "El cliente fue creado exitosamente.")
        return super().form_valid(form)

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Clients
    template_name = "app_service_watch/client_update.html"
    fields = ['name', 'last_name', 'email', 'company']
    success_url = reverse_lazy('Lista de Clientes')

    def form_valid(self, form):
        messages.success(self.request, "El cliente fue actualizado exitosamente.")
        return super().form_valid(form)
    
class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Clients
    template_name = "app_service_watch/client_delete.html"
    success_url = reverse_lazy('Lista de Clientes')

class StaffListView(LoginRequiredMixin, ListView):
    model = Staff
    template_name = "app_service_watch/staff_list.html"

class StaffDetailView (LoginRequiredMixin, DetailView):
    model = Staff
    template_name = "app_service_watch/staff_detail.html"

class StaffCreateView(LoginRequiredMixin, CreateView):
    model = Staff
    template_name = "app_service_watch/staff_create.html"
    fields = ['name', 'last_name', 'email']
    success_url = reverse_lazy('Lista de Staff')
    
    def form_valid(self, form):
        messages.success(self.request, "El empleado fue creado exitosamente.")
        return super().form_valid(form)

class StaffUpdateView (LoginRequiredMixin, UpdateView):
    model = Staff
    template_name = "app_service_watch/staff_update.html"
    fields = ['name', 'last_name', 'email']
    success_url = reverse_lazy('Lista de Staff')

    def form_valid(self, form):
        messages.success(self.request, "El empleado fue actualizado exitosamente.")
        return super().form_valid(form)

class StaffDeleteView(LoginRequiredMixin, DeleteView):
    model = Staff
    template_name = "app_service_watch/staff_delete.html"
    success_url = reverse_lazy('Lista de Staff')

class PendingServicesListView(LoginRequiredMixin, ListView):
    model = PendingServices
    template_name = "app_service_watch/pending_services_list.html"

class PendingServicesDetailView (LoginRequiredMixin, DetailView):
    model = PendingServices
    template_name = "app_service_watch/pending_services_detail.html"

class PendingServicesCreateView(LoginRequiredMixin, CreateView):
    model = PendingServices
    template_name = "app_service_watch/pending_services_create.html"
    fields = ['name', 'status_update_date', 'status']
    success_url = reverse_lazy('Lista de Servicios en Curso')
    
    def form_valid(self, form):
        messages.success(self.request, "El servicio fue creado exitosamente.")
        return super().form_valid(form)

class PendingServicesUpdateView (LoginRequiredMixin, UpdateView):
    model = PendingServices
    template_name = "app_service_watch/pending_services_update.html"
    fields = ['name', 'status_update_date', 'status']
    success_url = reverse_lazy('Lista de Servicios en Curso')

    def form_valid(self, form):
        messages.success(self.request, "El servicio fue actualizado exitosamente.")
        return super().form_valid(form)

class PendingServicesDeleteView(LoginRequiredMixin, DeleteView):
    model = PendingServices
    template_name = "app_service_watch/pending_services_delete.html"
    success_url = reverse_lazy('Lista de Servicios en Curso')

class ServicesProvidedListView(LoginRequiredMixin, ListView):
    model = ServicesProvided
    template_name = "app_service_watch/services_provided_list.html"

class ServicesProvidedDetailView (LoginRequiredMixin, DetailView):
    model = ServicesProvided
    template_name = "app_service_watch/services_provided_detail.html"

class ServicesProvidedCreateView(LoginRequiredMixin, CreateView):
    model = ServicesProvided
    template_name = "app_service_watch/services_provided_create.html"
    fields = ['name', 'completion_date', 'completed']
    success_url = reverse_lazy('Lista de Servicios Prestados')
    
    def form_valid(self, form):
        messages.success(self.request, "El servicio fue creado exitosamente.")
        return super().form_valid(form)

class ServicesProvidedUpdateView (LoginRequiredMixin, UpdateView):
    model = ServicesProvided
    template_name = "app_service_watch/services_provided_update.html"
    fields = ['name', 'completion_date', 'completed']
    success_url = reverse_lazy('Lista de Servicios Prestados')

    def form_valid(self, form):
        messages.success(self.request, "El servicio fue actualizado exitosamente.")
        return super().form_valid(form)

class ServicesProvidedDeleteView(LoginRequiredMixin, DeleteView):
    model = ServicesProvided
    template_name = "app_service_watch/services_provided_delete.html"
    success_url = reverse_lazy('Lista de Servicios Prestados')
     
def clients(request):

    get_clients = Clients.objects.all()

    return render(request, "app_service_watch/clients.html", {"get_clients":get_clients})

@login_required
def clients_form(request):
    
    if request.method == 'POST':
        
        clientsForm = ClientsForm(request.POST)

        print(clientsForm)

        if clientsForm.is_valid():

            informacion = clientsForm.cleaned_data    

            clients_form = Clients(name=informacion['name'], last_name=informacion['last_name'],email=informacion['email'], company=informacion['company'])

            clients_form.save()

        return render(request, "app_service_watch/index.html")
    
    else:
        clientsForm = ClientsForm()

    return render(request, "app_service_watch/clients_form.html", {"clientsForm": clientsForm})

@login_required
def staff(request):

    get_staff = Staff.objects.all()

    return render(request, "app_service_watch/staff.html", {"get_staff" : get_staff})

@login_required
def staff_form(request):
    
    if request.method == 'POST':
        
        staffForm = StaffForm(request.POST)

        print(staffForm)

        if staffForm.is_valid():

            informacion = staffForm.cleaned_data    

            staff_form = Staff(name=informacion['name'], last_name=informacion['last_name'],email=informacion['email'])

            staff_form.save()

        return render(request, "app_service_watch/index.html")
    
    else:
        staffForm = StaffForm()

    return render(request, "app_service_watch/staff_form.html", {"staffForm": staffForm})

def services_provided(request):
    
    serv_prov = ServicesProvided.objects.all()

    return render(request, "app_service_watch/services_provided.html", {"servicios_prestados" : serv_prov})

@login_required
def services_provided_form(request):
    
    if request.method == 'POST':
        
        spForm = ServicesProvidedForm(request.POST)

        print(spForm)

        if spForm.is_valid():

            informacion = spForm.cleaned_data    

            serv_prov_form = ServicesProvided(name=informacion['name'], completion_date=informacion['completion_date'],completed=informacion['completed'])

            serv_prov_form.save()

        return render(request, "app_service_watch/index.html")
    
    else:
        spForm = ServicesProvidedForm()

    return render(request, "app_service_watch/services_provided_form.html", {"spForm": spForm})

def pending_services(request):

    pend_serv = PendingServices.objects.all()

    return render(request, "app_service_watch/pending_services.html", {"servicios_pendientes" : pend_serv})

@login_required
def pending_services_form(request):
    
    if request.method == 'POST':
        
        psForm = PendingServicesForm(request.POST)

        print(psForm)

        if psForm.is_valid():

            informacion = psForm.cleaned_data

            pend_serv_form = PendingServices(name=informacion['name'], status_update_date=informacion['status_update_date'], status=informacion['status'])

            pend_serv_form.save()

        return render(request, "app_service_watch/index.html")
    
    else:
        psForm = PendingServicesForm()

    return render(request, "app_service_watch/pending_services_form.html", {"psForm": psForm})

def search(request):

    if request.method == "POST":

        miFormulario = Search(request.POST)

        if miFormulario.is_valid():
            
            info = miFormulario.cleaned_data
            
            busquedaserv = ServicesProvided.objects.filter(name__icontains=info["name"]) 
            
            return render(request, "app_service_watch/search.html", {"busquedaserv": busquedaserv })
    else:
        miFormulario = Search()

    return render(request, "app_service_watch/search.html", {"formulario": miFormulario})

def about(request):
    return render(request, "app_service_watch/about.html")
