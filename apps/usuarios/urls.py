from django.conf.urls import url
from apps.usuarios.views import RegistroUsuarios

urlpatterns =[
    url(r'^registrar', RegistroUsuarios.as_view(), name='registrar')

]