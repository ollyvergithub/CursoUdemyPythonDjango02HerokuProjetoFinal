from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_url

from django.conf import settings
from django.conf.urls.static import static
# Ollyver Coloquei estas 2 linhas ao invés da linha de baixo para funcionar
from django.contrib.auth.views import LoginView # Dedo Ollyver
from django.contrib.auth.views import LogoutView # Dedo Ollyver
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Ollyver Coloquei estas 2 linhas ao invés das duas de baixo para funcionar
    # Referencia: https://www.schoolofnet.com/forum/topico/modulo-djangocontribauthviews-nao-possui-atributo-chamado-login-7032
    #path('login/', LoginView.as_view(), name="login"), # Dedo Ollyver
    #path('logout/', LogoutView.as_view(), name="logout"), # Dedo Ollyver
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    #path('login/', auth_views.login, name='login'),
    #path('login/', auth_views.logout, name='logout'),

    path('clientes/', include(clientes_url)),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
