from django.urls import path, include
from users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
path("login", views.login_request, name="Login"),
path("register", views.register, name="Register"),
path("logout", LogoutView.as_view(template_name="app_service_watch/index.html"), name="Logout"),
path('editar_usuario/', views.editar_perfil, name='EditarUsuario'),
path('agregar_avatar/', views.agregar_avatar, name='AgregarAvatar'),
]
