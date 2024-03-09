from django.contrib import admin
from app_service_watch.models import *

admin.site.register(Clients)
admin.site.register(Staff)
admin.site.register(ServicesProvided)
admin.site.register(PendingServices)