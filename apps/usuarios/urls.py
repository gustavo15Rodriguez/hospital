from django.conf.urls import url
from apps.usuarios.views import UsuarioCrear

urlpatterns = [
    url(r'^$', UsuarioCrear.as_view(), name='registro'),
]