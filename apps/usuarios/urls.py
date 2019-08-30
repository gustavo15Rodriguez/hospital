from django.conf.urls import url
from apps.usuarios.views import UsuarioCrear

urlpatterns = [
    url(r'^registro/', UsuarioCrear.as_view(), name='registro'),
]