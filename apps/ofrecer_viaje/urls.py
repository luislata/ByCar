from django.conf.urls import url, include

from apps.ofrecer_viaje.views import index, ofrecer_viaje_view, ofrecerviaje_list, ofrecerviaje_edit, ofrecerviaje_delete, \
    ofrecerviajelist, ofrecerviajecreate, ofrecerviajeupdate, ofrecerviajedelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', ofrecerviajecreate.as_view(), name='crear_viaje'),
    url(r'^listar$', ofrecerviajelist.as_view(), name='listar_viaje'),
    url(r'^eliminar/(?P<pk>\d+)/$', ofrecerviajedelete.as_view(), name='viaje_eliminar'),
    url(r'editar/(?P<pk>\d+)/$', ofrecerviajeupdate.as_view(), name='ofrecerviaje_editar'),

]