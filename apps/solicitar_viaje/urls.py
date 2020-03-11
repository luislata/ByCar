from django.conf.urls import url

from apps.solicitar_viaje.views import index_Solicitar


urlpatterns = [
    url(r'^$',index_Solicitar)
]