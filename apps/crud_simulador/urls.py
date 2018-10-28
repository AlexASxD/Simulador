from django.conf.urls import url
from apps.crud_simulador.views import perfilCreate, perfilList, perfilUpdate, perfilDelete, perfilShow, search, mocvCreate,mocvList,mocvDelete,mocvShow,mocvUpdate,buscarxd\
    ,datos_empresaCreate, datos_empresaList, datos_empresaDelete, datos_empresaUpdate,datos_empresaShow, searchluis, manoObraCreate,manoObralist,manoObraDelete,manoObraUpdate\
    ,manoObraShow,conceptoCrecimientoDemandaCreate,conceptoCrecimientoDemandalist,conceptoCrecimientoDemandaDelete,conceptoCrecimientoDemandaUpdate, conceptoCrecimientoDemandaShow, searchluis2, searchluis3,\
    estimacion_serviciosCreate, estimacion_serviciosList,estimacion_serviciosDelete,estimacion_serviciosUpdate,estimacion_serviciosShow, tipoGastoOperativoCreate, tipoGastoOperativoList, tipoGastoOperativoDelete, tipoGastoOperativoUpdate, tipoGastoOperativoShow, searchever, searchever1\
    ,costosCreate,costosList,costosDelete,costosUpdate,costosShow,searchc,gastosCreate,gastosList,gastosDelete,gastosUpdate,gastosShow,findg\
    ,productoCreate,productoList,productoDelete,productoUpdate,productoShow,buscaP,gastossCreate,gastossList,gastossDelete,gastossUpdate,gastossShow,search_g\
    ,crecimientoDemandaCreate,crecimientoDemandaList,crecimientoDemandaDelete,crecimientoDemandaUpdate,crecimientoDemandaShow,search_c\
    ,tipoUsuarioCreate,tipoUsuarioList,tipoUsuarioDelete,tipoUsuarioUpdate,tipoUsuarioShow, search_u,gastosIndirectosCreate,gastosIndirectosList,gastosIndirectosDelete,gastosIndirectosUpdate,gastosIndirectosShow,search_a\
    ,tiposGastoscreate,tiposGastosList,tiposGastosDelete,tiposGastosUpdate,tiposGastosShow,search_b,usuarioCreate,usuarioList,usuarioDelete,usuarioShow,usuarioUpdate,search_tg, materiaPrimaCreate, materiaPrimaList,materiaPrimaDelete,materiaPrimaShow,materiaPrimaUpdate,search_ma,estimacionCreate\
    ,estimacionList,estimacionDelete,estimacionShow,estimacionUpdate,search_es,tiposInversionesCreate,tiposInversionesList,tiposInversionesDelete,tiposInversionesUpdate,tiposInversionesShow,search_ti

urlpatterns = [
    #urls de alex perfil usuario y mano de obra comision venta
    url(r'^crear/', perfilCreate.as_view(), name='perfil_crear'),
    url(r'^listar/', perfilList.as_view(), name='perfil_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', perfilDelete.as_view(), name='perfil_eliminar'),
    url(r'^modificar/(?P<pk>\d+)/$', perfilUpdate.as_view(), name='perfil_modificar'),
    url(r'^mostrar/(?P<pk>\d+)/$', perfilShow.as_view(), name='perfil_mostrar'),
    url(r'^buscar/$', search, name='perfil_buscar'),

    url(r'^create/',mocvCreate.as_view(), name='mocv_create'),
    url(r'^list/', mocvList.as_view(), name='mocv_list'),
    url(r'^delete/(?P<pk>\d+)/$', mocvDelete.as_view(), name='mocv_delete'),
    url(r'^update/(?P<pk>\d+)/$', mocvUpdate.as_view(), name='mocv_update'),
    url(r'^show/(?P<pk>\d+)/$', mocvShow.as_view(), name='mocv_show'),
    url(r'^search/$', buscarxd, name='mocv_search'),

    #urls de luis david
    url(r'^crearempresa/', datos_empresaCreate.as_view(), name='datos_empresa_crear'),
    url(r'^listarempresa/', datos_empresaList.as_view(), name='datos_empresa_listar'),
    url(r'^eliminarempresa/(?P<pk>\d+)/$', datos_empresaDelete.as_view(), name='datos_empresa_eliminar'),
    url(r'^editarempresa/(?P<pk>\d+)/$', datos_empresaUpdate.as_view(), name='datos_empresa_editar'),
    url(r'^mostrarempresa/(?P<pk>\d+)/$', datos_empresaShow.as_view(), name='datos_empresa_mostrar'),
    url(r'^buscarempresa/$', searchluis, name='datos_empresa_buscar'),

    url(r'^crearobra/', manoObraCreate.as_view(), name='manoObra_crear'),
    url(r'^guardarobra/', manoObralist.as_view(), name='manoObra_listar'),
    url(r'^eliminarobra/(?P<pk>\d+)/$', manoObraDelete.as_view(), name='manoObra_eliminar'),
    url(r'^modificarobra/(?P<pk>\d+)/$', manoObraUpdate.as_view(), name='manoObra_editar'),
    url(r'^observarobra/(?P<pk>\d+)/$', manoObraShow.as_view(), name='manoObra_mostrar'),
    url(r'^investigarobra/$', searchluis2, name='manoObra_buscar'),

    url(r'^nuevosccd/', conceptoCrecimientoDemandaCreate.as_view(), name='conceptoCrecimientoDemanda_crear'),
    url(r'^listasccd/', conceptoCrecimientoDemandalist.as_view(), name='conceptoCrecimientoDemanda_listar'),
    url(r'^eliminacionccd/(?P<pk>\d+)/$', conceptoCrecimientoDemandaDelete.as_view(), name='conceptoCrecimientoDemanda_eliminar'),
    url(r'^modificacionccd/(?P<pk>\d+)/$', conceptoCrecimientoDemandaUpdate.as_view(), name='conceptoCrecimientoDemanda_editar'),
    url(r'^verccd/(?P<pk>\d+)/$', conceptoCrecimientoDemandaShow.as_view(), name='conceptoCrecimientoDemanda_mostrar'),
    url(r'^buscadorccd/$', searchluis3, name='conceptoCrecimientoDemanda_buscar'),

    #Urls de Everardo
    url(r'^nuevoservicio/', estimacion_serviciosCreate.as_view(), name='estimacion_servicio_crear'),
    url(r'^listarservicio/', estimacion_serviciosList.as_view(), name='estimacion_servicio_listar'),
    url(r'^eliminarservicio/(?P<pk>\d+)/$', estimacion_serviciosDelete.as_view(), name='estimacion_servicio_eliminar'),
    url(r'^modificarservicio/(?P<pk>\d+)/$', estimacion_serviciosUpdate .as_view(), name='estimacion_servicio_editar'),
    url(r'^mostrarservicio/(?P<pk>\d+)/$', estimacion_serviciosShow.as_view(), name='estimacion_servicio_mostrar'),
    url(r'^buscarservicio/', searchever, name='estimacion_servicio_buscar'),

    url(r'^newtgasto/',tipoGastoOperativoCreate.as_view(), name='tipoGastoOperativo_crear'),
    url(r'^listgasto/',tipoGastoOperativoList.as_view(), name='tipoGastoOperativo_listar'),
    url(r'^deletegasto/(?P<pk>\d+)/$',tipoGastoOperativoDelete.as_view(), name='tipoGastoOperativo_eliminar'),
    url(r'^updategasto/(?P<pk>\d+)/$',tipoGastoOperativoUpdate.as_view(), name='tipoGastoOperativo_editar'),
    url(r'^showgasto/(?P<pk>\d+)/$',tipoGastoOperativoShow.as_view(), name='tipoGastoOperativo_mostrar'),
    url(r'^searchgasto/$', searchever1, name='tipoGastoOperativo_buscar'),

 #urls de carmen
    url(r'^nuevoC/', costosCreate.as_view(), name='costos_crear'),
    url(r'^listarC/', costosList.as_view(), name='costos_listar'),
    url(r'^eliminarC/(?P<pk>\d+)/$', costosDelete.as_view(), name='costos_eliminar'),
    url(r'^modificarC/(?P<pk>\d+)/$', costosUpdate.as_view(), name='costos_editar'),
    url(r'^mostrarC/(?P<pk>\d+)/$', costosShow.as_view(), name='costos_mostrar'),
    url(r'^buscarC/$', searchc, name='costos_buscar'),

    url(r'^nuevoG/', gastosCreate.as_view(), name='gastos_crear'),
    url(r'^listarG/', gastosList.as_view(), name='gastos_listar'),
    url(r'^eliminarG/(?P<pk>\d+)/$', gastosDelete.as_view(), name='gastos_eliminar'),
    url(r'^modificarG/(?P<pk>\d+)/$', gastosUpdate.as_view(), name='gastos_editar'),
    url(r'^mostrarG/(?P<pk>\d+)/$', gastosShow.as_view(), name='gastos_mostrar'),
    url(r'^buscarG/$', findg, name='gastos_buscar'),

    url(r'^nuevoP/', productoCreate.as_view(), name='producto_crear'),
    url(r'^listarP/', productoList.as_view(), name='producto_listar'),
    url(r'^eliminarP/(?P<pk>\d+)/$', productoDelete.as_view(), name='producto_eliminar'),
    url(r'^modificarP/(?P<pk>\d+)/$', productoUpdate.as_view(), name='producto_editar'),
    url(r'^mostrarP/(?P<pk>\d+)/$', productoShow.as_view(), name='producto_mostrar'),
    url(r'^buscarP/$', buscaP, name='producto_buscar'),

#Urls de Alan
    url(r'^nuevogastos/',gastossCreate.as_view(), name='gastoss_crear'),
    url(r'^listargastos/',gastossList.as_view(),name='gastoss_listar'),
    url(r'^eliminargastos/(?P<pk>\d+)/$', gastossDelete.as_view(), name='gastoss_eliminar'),
    url(r'^editargastos/(?P<pk>\d+)/$', gastossUpdate.as_view(), name='gastoss_editar'),
    url(r'^mostrargastos/(?P<pk>\d+)/$', gastossShow.as_view(), name='gastoss_mostrar'),
    url(r'^buscargastos/$', search_g, name='gastoss_buscar'),

    url(r'^newcrecimiento/',crecimientoDemandaCreate.as_view(), name='crecimientoDemanda_crear'),
    url(r'^listcrecimiento/',crecimientoDemandaList.as_view(),name='crecimientoDemanda_listar'),
    url(r'^deletecrecimiento/(?P<pk>\d+)/$', crecimientoDemandaDelete.as_view(), name='crecimientoDemanda_eliminar'),
    url(r'^updatecrecimiento/(?P<pk>\d+)/$', crecimientoDemandaUpdate.as_view(), name='crecimientoDemanda_editar'),
    url(r'^showcrecimiento/(?P<pk>\d+)/$', crecimientoDemandaShow.as_view(), name='crecimientoDemanda_mostrar'),
    url(r'^searchcrecimiento/$', search_c, name='crecimientoDemanda_buscar'),

    url(r'^nuevostipou/',tipoUsuarioCreate.as_view(), name='tipoUsuario_crear'),
    url(r'^listastipou/',tipoUsuarioList.as_view(),name='tipoUsuario_listar'),
    url(r'^eliminaciontipou/(?P<pk>\d+)/$', tipoUsuarioDelete.as_view(), name='tipoUsuario_eliminar'),
    url(r'^modificartipou/(?P<pk>\d+)/$', tipoUsuarioUpdate.as_view(), name='tipoUsuario_editar'),
    url(r'^vertipou/(?P<pk>\d+)/$', tipoUsuarioShow.as_view(), name='tipoUsuario_mostrar'),
    url(r'^buscadortipou/$', search_u, name='tipoUsuario_buscar'),

#Urls de Emmanuel

url(r'^nuevoGI/', gastosIndirectosCreate.as_view(), name='gastosIndirectos_crear'),
    url(r'^listaGI/', gastosIndirectosList.as_view(), name='gastosIndirectos_listar'),
    url(r'^eliminarGI/(?P<pk>\d+)/$', gastosIndirectosDelete.as_view(), name='gastosIndirectos_eliminar'),
    url(r'^editaGI/(?P<pk>\d+)/$', gastosIndirectosUpdate.as_view(), name='gastosIndirectos_editar'),
    url(r'^mostrarGI/(?P<pk>\d+)/$', gastosIndirectosShow.as_view(), name='gastosIndirectos_mostrar'),
    url(r'^buscarGI/$', search_a, name='gastosIndirectos_buscar'),

    url(r'^nuevostg/', tiposGastoscreate.as_view(), name='tiposGastos_crear'),
    url(r'^listartg/', tiposGastosList.as_view(), name='tiposGastos_listar'),
    url(r'^eliminarrtg/(?P<pk>\d+)/$', tiposGastosDelete.as_view(), name='tiposGastos_eliminar'),
    url(r'^editartg/(?P<pk>\d+)/$', tiposGastosUpdate.as_view(), name='tiposGastos_editar'),
    url(r'^mostratg/(?P<pk>\d+)/$', tiposGastosShow.as_view(), name='tiposGastos_mostrar'),
    url(r'^buscatg/$', search_b, name='tiposGastos_buscar'),


    url(r'^nuevossusuario/', usuarioCreate.as_view(), name='usuario_crear'),
    url(r'^listassusuario/', usuarioList.as_view(), name='usuario_listar'),
    url(r'^eliminausuario/(?P<pk>\d+)/$', usuarioDelete.as_view(), name='usuario_eliminar'),
    url(r'^editarrusuario/(?P<pk>\d+)/$', usuarioUpdate.as_view(), name='usuario_editar'),
    url(r'^mostrarrusuario/(?P<pk>\d+)/$', usuarioShow.as_view(), name='usuario_mostrar'),
    url(r'^buscarrusuario/$', search_tg, name='usuario_buscar'),

#urls de aldair
    url(r'^nuevomat/', materiaPrimaCreate.as_view(), name='materiaPrima_crear'),
    url(r'^listamat/', materiaPrimaList.as_view(), name='materiaPrima_listar'),
    url(r'^eliminamat/(?P<pk>\d+)/$', materiaPrimaDelete.as_view(), name='materiaPrima_eliminar'),
    url(r'^editamat/(?P<pk>\d+)/$', materiaPrimaUpdate.as_view(), name='materiaPrima_editar'),
    url(r'^muestramat/(?P<pk>\d+)/$', materiaPrimaShow.as_view(), name='materiaPrima_mostrar'),
    url(r'^buscamat/$', search_ma, name='materiaPrima_buscar'),

    url(r'^nuevoses/', estimacionCreate.as_view(), name='estimacion_crear'),
    url(r'^listases/', estimacionList.as_view(), name='estimacion_listar'),
    url(r'^eliminares/(?P<pk>\d+)/$', estimacionDelete.as_view(), name='estimacion_eliminar'),
    url(r'^editares/(?P<pk>\d+)/$', estimacionUpdate.as_view(), name='estimacion_editar'),
    url(r'^mostrares/(?P<pk>\d+)/$', estimacionShow.as_view(), name='estimacion_mostrar'),
    url(r'^buscares/$', search_es, name='estimacion_buscar'),

    url(r'^nuevastip/', tiposInversionesCreate.as_view(), name='tiposInversiones_crear'),
    url(r'^listastip/', tiposInversionesList.as_view(), name='tiposInversiones_listar'),
    url(r'^eliminastip/(?P<pk>\d+)/$', tiposInversionesDelete.as_view(), name='tiposInversiones_eliminar'),
    url(r'^editastip/(?P<pk>\d+)/$', tiposInversionesUpdate.as_view(), name='tiposInversiones_editar'),
    url(r'^muestrastip/(?P<pk>\d+)/$', tiposInversionesShow.as_view(), name='tiposInversiones_mostrar'),
    url(r'^buscasip/$', search_ti, name='tiposInversiones_buscar'),
]