from apps.principal.views import index
from django.conf.urls import url

urlpatterns = [
    url(r'$', index, name='home'),
]