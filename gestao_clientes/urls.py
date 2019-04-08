"""gestao_clientes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_url

from django.conf import settings
from django.conf.urls.static import static
# Ollyver Coloquei estas 2 linhas ao invés da linha de baixo para funcionar
from django.contrib.auth.views import LoginView # Dedo Ollyver
from django.contrib.auth.views import LogoutView # Dedo Ollyver
#from django.contrib.auth import views as auth_views

urlpatterns = [
    # Ollyver Coloquei estas 2 linhas ao invés das duas de baixo para funcionar
    # Referencia: https://www.schoolofnet.com/forum/topico/modulo-djangocontribauthviews-nao-possui-atributo-chamado-login-7032
    path('login/', LoginView.as_view(), name="login"), # Dedo Ollyver
    path('logout/', LogoutView.as_view(), name="logout"), # Dedo Ollyver
    #path('login/', auth_views.login, name='login'),
    #path('login/', auth_views.logout, name='logout'),

    path('clientes/', include(clientes_url)),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
