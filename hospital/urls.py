"""hospital URL Configuration

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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, logout_then_login, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView
from django.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^registro/', include('apps.usuarios.urls')),
    url(r'^administracion/', include('apps.administracion.urls')),
    url(r'^doctores/', include('apps.doctores.urls')),
    url(r'^pacientes/', include('apps.pacientes.urls')),
    url(r'^home/', include('apps.principal.urls')),

    #Recuperacion de Email
    url(r'^password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password_reset/', PasswordResetView.as_view(), name='password_reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_ \-]+)/(?P<token>.+)/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^accounts/login/', LoginView.as_view(template_name='index.html'), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

