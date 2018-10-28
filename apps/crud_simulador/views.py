from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from apps.crud_simulador.models import perfil_usuario, manoObraComisionesVenta, datos_empresa, manoObra , conceptoCrecimientoDemanda, estimacion_servicios, tipoGastoOperativo, costosTotalesAnuales,tiposGastoss,producto_servicio, gastos, crecimientoDemanda,tipoUsuario,gastosIndirectos,Usuario, tiposGastos, tiposInversiones,materiaPrimaInsumos,estimacion_crecimiento_anual
from apps.crud_simulador.forms import perfilusuarioForm, ManoObraCventaForm,datos_empresaForm, manoObraForm, conceptoCrecimientoDemandaForm, estimacion_serviciosForm, tipoGastoOperativoForms,costototalForm,tiposGastosForm,tiposgastosForm,productoSForm,gastosForm,crecimientoDemandaForm, tipoUsuarioForm,gastosIndirectosForm, usuarioForm,estimacionForm,materiaPrimaForm,tiposInversionesForm
from apps.crud_simulador.filters import perfilFilter,McomisionesVFilter,datos_empresaFilter, manoObraFilter, conceptoCrecimientoDemandaFilter, estimacion_serviciosFilter, tipoGastoOperativoFilter,costosFilter,tiposGastosFilter,tipoUsuarioFilter,productoFilter,gastosFilter,gastossFilter,crecimientoDemandaFilter,gastosIndirectosFilter,usuarioFilter,estimacionFilter,materiaPrimaFilter,tiposInversionesFilter
from django.urls import reverse_lazy

#clases del perfil usuario

class perfilCreate(CreateView):
    model = perfil_usuario
    form_class = perfilusuarioForm
    template_name = 'formularios/perfil_form.html'
    success_url = reverse_lazy('perfil_usuario:perfil_crear')

class perfilList(ListView):
    queryset = perfil_usuario.objects.order_by('nombre_usuario')
    template_name = 'formularios/perfil_list.html'
    paginate_by = 100

class perfilUpdate(UpdateView):
    model = perfil_usuario
    form_class = perfilusuarioForm
    template_name = 'formularios/perfil_form.html'
    success_url = reverse_lazy('perfil_usuario:perfil_listar')

class perfilDelete(DeleteView):
    model = perfil_usuario
    template_name = 'formularios/perfil_delete.html'
    success_url = reverse_lazy('perfil_usuario:perfil_listar')

class perfilShow(DetailView):
    model = perfil_usuario
    template_name = 'formularios/perfil_show.html'

def search(request):
    perfil_list = perfil_usuario.objects.all()
    perfil_filter = perfilFilter(request.GET, queryset=perfil_list)
    return render(request, 'formularios/perfil_list_filter.html', {'filter': perfil_filter})

class mocvCreate(CreateView):
    model = manoObraComisionesVenta
    form_class = ManoObraCventaForm
    template_name = 'formularios/mocv_form.html'
    success_url = reverse_lazy('mcomisiones:mocv_create')

class mocvList(ListView):
    queryset = manoObraComisionesVenta.objects.order_by('idmanoObraComisionesVenta')
    template_name = 'formularios/mocv_list.html'
    paginate_by = 100

class mocvUpdate(UpdateView):
    model = perfil_usuario
    form_class = perfilusuarioForm
    template_name = 'formularios/mocv_form.html'
    success_url = reverse_lazy('mcomisiones:mocv_list')

class mocvDelete(DeleteView):
    model = manoObraComisionesVenta
    template_name = 'formularios/mocv_delete.html'
    success_url = reverse_lazy('mcomisiones:mocv_list')

class mocvShow(DetailView):
    model = manoObraComisionesVenta
    template_name = 'formularios/mocv_show.html'

def buscarxd(request):
    manoxd_list = manoObraComisionesVenta.objects.all()
    manoxd_filter = McomisionesVFilter(request.GET, queryset=manoxd_list)
    return render(request, 'formularios/mocv_list_filter.html', {'filter': manoxd_filter})

#Views de luis david :v

class datos_empresaCreate(CreateView):
    model = datos_empresa
    form_class = datos_empresaForm
    template_name =  'crudsimuladornegocios/simulador_form.html'
    success_url = reverse_lazy('simulador : simulador_listar')

class datos_empresaList(ListView):
        queryset = datos_empresa.objects.order_by('id_empresa')
        template_name = 'crudsimuladornegocios/simulador_list.html'

class datos_empresaUpdate(UpdateView):
    model = datos_empresa
    form_class = datos_empresaForm
    template_name = 'crudsimuladornegocios/simulador_form.html'
    success_url = reverse_lazy('crudsimuladornegocios:simulador_listar')


class datos_empresaDelete(DeleteView):
    model = datos_empresa
    template_name = 'crudsimuladornegocios/simulador_delete.html'
    success_url = reverse_lazy('crudsimuladornegocios:simulador_listar')

class datos_empresaShow(DetailView):
    model = datos_empresa
    template_name = 'crudsimuladornegocios/simulador_show.html'

def searchluis(request):
    datos_list = datos_empresa.objects.all()
    datos_filter = datos_empresaFilter(request.GET, queryset = datos_list)
    return render(request, 'crudsimuladornegocios/simulador_list_filter.html',{'filter': datos_filter})


class manoObraCreate(CreateView):
    model = manoObra
    form_class = manoObraForm
    template_name =  'crudsimuladornegocios/obra_form.html'
    success_url = reverse_lazy('obra:obra_listar')

class manoObralist(ListView):
        queryset = manoObra.objects.order_by('idManoObra')
        template_name = 'crudsimuladornegocios/obra_list.html'


class manoObraUpdate(UpdateView):
    model = manoObra
    form_class = manoObraForm
    template_name = 'crudsimuladornegocios/obra_form.html'
    success_url = reverse_lazy('crudsimuladornegocios:obra_listar')


class manoObraDelete(DeleteView):
    model = manoObra
    template_name = 'crudsimuladornegocios/simulador_delete.html'
    success_url = reverse_lazy('crudsimuladornegocios:obra_listar')

class manoObraShow(DetailView):
    model = manoObra
    template_name = 'crudsimuladornegocios/obra_show.html'

def searchluis2(request):
    mano_list = manoObra.objects.all()
    mano_filter = manoObraFilter(request.GET, queryset = mano_list)
    return render(request, 'crudsimuladornegocios/obra_list_filter.html',{'filter': mano_filter})


class conceptoCrecimientoDemandaCreate(CreateView):
    model = conceptoCrecimientoDemanda
    form_class = conceptoCrecimientoDemandaForm
    template_name = 'crudsimuladornegocios/crecimiento_form.html'
    success_url = reverse_lazy('demanda:conceptoCrecimientoDemanda_listar')


class conceptoCrecimientoDemandalist(ListView):
    queryset = conceptoCrecimientoDemanda.objects.order_by('idccd')
    template_name = 'crudsimuladornegocios/crecimiento_list.html'


class conceptoCrecimientoDemandaUpdate(UpdateView):
    model = manoObra
    form_class = conceptoCrecimientoDemandaForm
    template_name = 'crudsimuladornegocios/simulador_form.html'
    success_url = reverse_lazy('demanda:conceptoCrecimientoDemanda_listar')


class conceptoCrecimientoDemandaDelete(DeleteView):
    model = conceptoCrecimientoDemanda
    template_name = 'crudsimuladornegocios/simulador_delete.html'
    success_url = reverse_lazy('demanda:conceptoCrecimientoDemanda_listar')


class conceptoCrecimientoDemandaDetail(DetailView):
    model = conceptoCrecimientoDemanda
    template_name = 'crudsimuladornegocios/crecimiento_show.html'

class conceptoCrecimientoDemandaShow(DetailView):
    model = conceptoCrecimientoDemanda
    template_name = 'crudsimuladornegocios/crecimiento_show.html'


def searchluis3(request):
    crecimientolist = conceptoCrecimientoDemanda.objects.all()
    crecimiento_filter = conceptoCrecimientoDemandaFilter(request.GET, queryset=crecimientolist)
    return render(request, 'crudsimuladornegocios/crecimiento_list_filter.html', {'filter': crecimiento_filter})

#views de Everardo

class estimacion_serviciosCreate(CreateView):
    model = estimacion_servicios
    form_class = estimacion_serviciosForm
    template_name = 'crudestimacionservicios/estimacion_servicios_form.html'
    success_url = reverse_lazy('estimacion_servicios:estimacion_servicio_crear')

class estimacion_serviciosList(ListView):
    queryset =estimacion_servicios.objects.order_by('id_suscripcion')
    template_name = 'crudestimacionservicios/estimacion_servicios_list.html'

class estimacion_serviciosUpdate(UpdateView):
    model = estimacion_servicios
    form_class = estimacion_serviciosForm
    template_name = 'crudestimacionservicios/estimacion_servicios_form.html'
    success_url = reverse_lazy('estimacion_servicios:estimacion_servicios_listar')

class estimacion_serviciosDelete(DeleteView):
    model = estimacion_servicios
    template_name = 'crudestimacionservicios/estimacion_servicios_delete.html'
    success_url = reverse_lazy('estimacion_servicios:estimacion_servicio_listar')

class estimacion_serviciosShow(DetailView):
    model = estimacion_servicios
    template_name = 'crudestimacionservicios/estimacion_servicios_show.html'

def searchever(request):
    estimacion_sevicios_list = estimacion_servicios.objects.all()
    estimacion_sevicios_filter = estimacion_serviciosFilter(request.GET, queryset=estimacion_sevicios_list)
    return render(request, 'crudestimacionservicios/estimacion_servicios_list_filter.html', {'filter': estimacion_sevicios_filter})

class tipoGastoOperativoCreate(CreateView):
    model = tipoGastoOperativo
    form_class = tipoGastoOperativoForms
    template_name = 'crudestimacionservicios/tipoGastoOperativo_form.html'
    success_url = reverse_lazy('tipoGastoOperativo:tipoGastoOperativo_listar')


class tipoGastoOperativoList(ListView):
    queryset =tipoGastoOperativo.objects.order_by('idtipoGasto')
    template_name = 'crudestimacionservicios/tipoGastoOperativo_list.html'

class tipoGastoOperativoUpdate(UpdateView):
    model = tipoGastoOperativo
    form_class = tipoGastoOperativoForms
    template_name = 'crudestimacionservicios/tipoGastoOperativo_form.html'
    success_url = reverse_lazy('tipoGastoOperativo:tipoGastoOperativo_listar')

class tipoGastoOperativoDelete(DeleteView):
    model = tipoGastoOperativo
    template_name = 'crudestimacionservicios/tipoGastoOperativo_delete.html'
    success_url = reverse_lazy('tipoGastoOperativo:tipoGastoOperativo_listar')

class tipoGastoOperativoShow(DetailView):
    model = tipoGastoOperativo
    template_name = 'crudestimacionservicios/tipoGastoOperativo_show.html'

def searchever1(request):
    tipoGastoOperativo_list = tipoGastoOperativo.objects.all()
    tipoGastoOperativo_filter = tipoGastoOperativoFilter(request.GET, queryset=tipoGastoOperativo_list)
    return render(request, 'crudestimacionservicios/tipoGastoOperativo_list_filter.html', {'filter': tipoGastoOperativo_filter})

#views de carmen

class costosCreate(CreateView):
    model = costosTotalesAnuales
    form_class = costototalForm
    template_name = 'crud_costos/costos_form.html'
    success_url = reverse_lazy('costos:costos_listar')

class costosList(ListView):
    queryset = costosTotalesAnuales.objects.order_by('idcostosTotalesAnuales')
    template_name = 'crud_costos/costos_list.html'
    paginate_by = 100

class costosUpdate(UpdateView):
    model = costosTotalesAnuales
    form_class = costototalForm
    template_name = 'crud_costos/costos_form.html'
    success_url = reverse_lazy('costos:costos_listar')

class costosDelete(DeleteView):
    model = costosTotalesAnuales
    template_name = 'crud_costos/costos_delete.html'
    success_url = reverse_lazy('costos:costos_listar')

class costosShow(DetailView):
    model = costosTotalesAnuales
    template_name = 'crud_costos/costos_show.html'

def searchc(request):
    costos_list = costosTotalesAnuales.objects.all()
    costos_filter = costosFilter(request.GET, queryset=costos_list)
    return render(request, 'crud_costos/costos_list_filter.html', {'filter': costos_filter})


class gastosCreate(CreateView):
    model = tiposGastoss
    form_class = tiposgastosForm
    template_name = 'crud_costos/gastos_form.html'
    success_url = reverse_lazy('gastos:gastos_listar')

class gastosList(ListView):
    queryset = tiposGastoss.objects.order_by('idtiposGastoss')
    template_name = 'crud_costos/gastos_list.html'
    paginate_by = 100

class gastosUpdate(UpdateView):
    model = tiposGastoss
    form_class = tiposgastosForm
    template_name = 'crud_costos/gastos_form.html'
    success_url = reverse_lazy('gastos:gastos_listar')

class gastosDelete(DeleteView):
    model = tiposGastoss
    template_name = 'crud_costos/gastos_delete.html'
    success_url = reverse_lazy('gastos:gastos_listar')

class gastosShow(DetailView):
    model = tiposGastoss
    template_name = 'crud_costos/gastos_show.html'

def findg(request):
    gastos_list = tiposGastoss.objects.all()
    gastos_filter = gastossFilter(request.GET, queryset=gastos_list)
    return render(request, 'crud_costos/gastos_list_filter.html', {'filter': gastos_filter})


class productoCreate(CreateView):
    model = producto_servicio
    form_class = productoSForm
    template_name = 'crud_costos/producto_form.html'
    success_url = reverse_lazy('producto:producto_listar')

class productoList(ListView):
    queryset = producto_servicio.objects.order_by('producto_nombre')
    template_name = 'crud_costos/producto_list.html'
    paginate_by = 100

class productoUpdate(UpdateView):
    model = producto_servicio
    form_class = productoSForm
    template_name = 'crud_costos/producto_form.html'
    success_url = reverse_lazy('producto:producto_listar')

class productoDelete(DeleteView):
    model = producto_servicio
    template_name = 'crud_costos/producto_delete.html'
    success_url = reverse_lazy('producto:producto_listar')

class productoShow(DetailView):
    model = producto_servicio
    template_name = 'crud_costos/producto_show.html'


def buscaP(request):
    producto_list = producto_servicio.objects.all()
    producto_filter = productoFilter(request.GET, queryset=producto_list)
    return render(request, 'crud_costos/producto_list_filter.html', {'filter': producto_filter})

# views de alan

class gastossCreate(CreateView):
    model= gastos
    form_class = gastosForm
    template_name='crudgastos/gastos_form.html'
    success_url = reverse_lazy('gastoss:gastoss_listar')

class gastossList(ListView):
        queryset = gastos.objects.order_by('idgastos')
        template_name = 'crudgastos/gastos_list.html'
        paginate_by = 100

class gastossUpdate(UpdateView):
        model = gastos
        form_class = gastosForm
        template_name = 'crudgastos/gastos_form.html'
        success_url = reverse_lazy('gastoss:gastoss_listar')

class gastossDelete(DeleteView):
        model = gastos
        template_name = 'crudgastos/gastos_delete.html'
        success_url = reverse_lazy('gastoss:gastoss_listar')

class gastossShow(DetailView):
        model = gastos
        template_name = 'crudgastos/gastos_show.html'

def search_g(request):
    gastos_list = gastos.objects.all()
    gastos_filter = gastosFilter(request.GET, queryset=gastos_list)
    return render(request, 'crudgastos/gastos_list_filter.html', {'filter': gastos_filter})


class crecimientoDemandaCreate(CreateView):
    model= crecimientoDemanda
    form_class = crecimientoDemandaForm
    template_name= 'crudgastos/crecimientoDemanda_form.html'
    success_url = reverse_lazy('crecimientoDemanda:crecimientoDemanda_listar')

class crecimientoDemandaList(ListView):
        queryset = crecimientoDemanda.objects.order_by('idcrecimientoDemanda')
        template_name = 'crudgastos/crecimientoDemanda_list.html'
        paginate_by = 100

class crecimientoDemandaUpdate(UpdateView):
        model = crecimientoDemanda
        form_class = crecimientoDemandaForm
        template_name = 'crudgastos/crecimientoDemanda_form.html'
        success_url = reverse_lazy('crecimientoDemanda:crecimientoDemanda_listar')

class crecimientoDemandaDelete(DeleteView):
        model = crecimientoDemanda
        template_name = 'crudgastos/crecimientoDemanda_delete.html'
        success_url = reverse_lazy('crecimientoDemanda:crecimientoDemanda_listar')

class crecimientoDemandaShow(DetailView):
        model = crecimientoDemanda
        template_name = 'crudgastos/crecimientoDemanda_show.html'

def search_c(request):
    crecimientoDemanda_list = crecimientoDemanda.objects.all()
    crecimientoDemanda_filter = crecimientoDemandaFilter(request.GET, queryset=crecimientoDemanda_list)
    return render(request, 'crudgastos/crecimientoDemanda_list_filter.html', {'filter': crecimientoDemanda_filter})

class tipoUsuarioCreate(CreateView):
    model= tipoUsuario
    form_class = tipoUsuarioForm
    template_name='crudgastos/tipoUsuario_form.html'
    success_url = reverse_lazy('tipoUsuario:tipoUsuario_listar')

class tipoUsuarioList(ListView):
        queryset = tipoUsuario.objects.order_by('idtipoUsuario')
        template_name = 'crudgastos/tipoUsuario_list.html'
        paginate_by = 100

class tipoUsuarioUpdate(UpdateView):
        model = tipoUsuario
        form_class = tipoUsuarioForm
        template_name = 'crudgastos/tipoUsuario_form.html'
        success_url = reverse_lazy('tipoUsuario:tipoUsuario_listar')

class tipoUsuarioDelete(DeleteView):
        model = tipoUsuarioForm
        template_name = 'crudgastos/tipoUsuario_delete.html'
        success_url = reverse_lazy('tipoUsuario:tipoUsuario_listar')

class tipoUsuarioShow(DetailView):
        model = tipoUsuarioForm
        template_name = 'crudgastos/tipoUsuario_show.html'

def search_u(request):
    tipoUsuario_list = tipoUsuario.objects.all()
    tipoUsuario_filter = tipoUsuarioFilter(request.GET, queryset=tipoUsuario_list)
    return render(request, 'crudgastos/tipoUsuario_list_filter.html', {'filter': tipoUsuario_filter})

#Views De Emmanuel

class gastosIndirectosCreate(CreateView):
    model = gastosIndirectos
    form_class = gastosIndirectosForm
    template_name = 'crudsimulador/gastosIndirectos_form.html'
    success_url = reverse_lazy('gastosIndirectos:gastosIndirectos_listar')

class gastosIndirectosList(ListView):
    queryset = gastosIndirectos.objects.order_by('idgastosIndirectos')
    template_name = 'crudsimulador/gastosIndirectos_list.html'

class gastosIndirectosUpdate(UpdateView):
    model = gastosIndirectos
    form_class = gastosIndirectosForm
    template_name = 'crudsimulador/gastosIndirectos_form.html'
    success_url = reverse_lazy('gastosIndirectos:gastosIndirectos_listar')

class gastosIndirectosDelete(DeleteView):
    model = gastosIndirectos
    template_name = 'crudsimulador/gastosIndirectos_delete.html'
    success_url = reverse_lazy('gastosIndirectos:gastosIndirectos_listar')

class gastosIndirectosShow(DetailView):
    model = gastosIndirectos
    template_name = 'crudsimulador/gastosIndirectos_show.html'

def search_a(request):
    gastosIndirectos_list = gastosIndirectos.objects.all()
    gastosIndirectos_filter = gastosIndirectosFilter(request.GET, queryset = gastosIndirectos_list)
    return render(request, 'crudsimulador/gastosIndirectos_list_filter.html',{'filter':gastosIndirectos_filter})


class usuarioCreate(CreateView):
    model = Usuario
    form_class = usuarioForm
    template_name = 'crudsimulador/usuario_form.html'
    success_url = reverse_lazy('usuario:usuario_listar')

class usuarioList(ListView):
    queryset = Usuario.objects.order_by('idusuario')
    template_name = 'crudsimulador/usuario_list.html'

class usuarioUpdate(UpdateView):
    model = Usuario
    form_class = usuarioForm
    template_name = 'crudsimulador/usuario_form.html'
    success_url = reverse_lazy('usuario:usuario_listar')

class usuarioDelete(DeleteView):
    model = Usuario
    template_name = 'crudsimulador/usuario_delete.html'
    success_url = reverse_lazy('usuario:usuario_listar')

class usuarioShow(DetailView):
    model = Usuario
    template_name = 'crudsimulador/usuario_show.html'

def search_b(request):
    usuario_list = Usuario.objects.all()
    usuario_filter = usuarioFilter(request.GET, queryset = usuario_list)
    return render(request, 'crudsimulador/usuario_list_filter.html', {'filter':usuario_filter})


class tiposGastoscreate(CreateView):
    model = tiposGastos
    form_class = tiposGastosForm
    template_name = 'crudsimulador/tiposGastos_form.html'
    success_url = reverse_lazy('tiposGastos:tiposGastos_listar')

class tiposGastosList(ListView):
    queryset = tiposGastos.objects.order_by('idtipoGastos')
    template_name = 'crudsimulador/tiposGastos_list.html'

class tiposGastosUpdate(UpdateView):
    model = tiposGastos
    form_class = tiposGastosForm
    template_name = 'crudsimulador/tiposGastos_form.html'
    success_url = reverse_lazy('tiposGastos:tiposGastos_listar')

class tiposGastosDelete(DeleteView):
    model = tiposGastos
    template_name = 'crudsimulador/tiposGastos_delete.html'
    success_url = reverse_lazy('tiposGastos:tiposGastos_listar')

class tiposGastosShow(DetailView):
    model = tiposGastos
    template_name = 'crudsimulador/tiposGastos_show.html'

def search_tg(request):
    tiposGastos_list = tiposGastos.objects.all()
    tiposGastos_filter = tiposGastosFilter(request.GET, queryset = tiposGastos_list)
    return render(request, 'crudsimulador/tiposGastos_list_filter.html', {'filter': tiposGastos_filter})

#views de litzy
class materiaPrimaCreate(CreateView):
    model = materiaPrimaInsumos
    form_class = materiaPrimaForm
    template_name = 'crudsimulador/materiaPrima_form.html'
    success_url = reverse_lazy('materiaPrima:materiaPrima_listar')

class materiaPrimaList(ListView):
    queryset = materiaPrimaInsumos.objects.order_by('idmateriaPrimaInsumos')
    template_name = 'crudsimulador/materiaPrima_list.html'

class materiaPrimaUpdate(UpdateView):
    model = materiaPrimaInsumos
    form_class = materiaPrimaForm
    template_name = 'crudsimulador/materiaPrima_form.html'
    success_url = reverse_lazy('materiaPrima:materiaPrima_listar')

class materiaPrimaDelete(DeleteView):
    model = materiaPrimaInsumos
    template_name = 'crudsimulador/materiaPrima_delete.html'
    success_url = reverse_lazy('materiaPrima:materiaPrima_listar')

class materiaPrimaShow(DetailView):
    model = materiaPrimaInsumos
    template_name = 'crudsimulador/materiaPrima_show.html'

def search_ma(request):
    materiaPrima_list = materiaPrimaInsumos.objects.all()
    materiaPrima_filter = materiaPrimaFilter(request.GET, queryset = materiaPrima_list)
    return render(request, 'crudsimulador/materiaPrima_list_filter.html',{'filter':materiaPrima_filter})


class estimacionCreate(CreateView):
    model = estimacion_crecimiento_anual
    form_class = estimacionForm
    template_name = 'crudsimulador/estimacion_form.html'
    success_url = reverse_lazy('estimacion:estimacion_listar')

class estimacionList(ListView):
    queryset = estimacion_crecimiento_anual.objects.order_by('numero_anio')
    template_name = 'crudsimulador/estimacion_list.html'

class estimacionUpdate(UpdateView):
    model = estimacion_crecimiento_anual
    form_class = estimacionForm
    template_name = 'crudsimulador/estimacion_form.html'
    success_url = reverse_lazy('estimacion:estimacion_listar')

class estimacionDelete(DeleteView):
    model = estimacion_crecimiento_anual
    template_name = 'crudsimulador/estimacion_delete.html'
    success_url = reverse_lazy('estimacion:estimacion_listar')

class estimacionShow(DetailView):
    model = estimacion_crecimiento_anual
    template_name = 'crudsimulador/estimacion_show.html'

def search_es(request):
    estimacion_list = estimacion_crecimiento_anual.objects.all()
    estimacion_filter = estimacionFilter(request.GET, queryset = estimacion_list)
    return render(request, 'crudsimulador/estimacion_list_filter.html', {'filter':estimacion_filter})




class tiposInversionesCreate(CreateView):
    model = tiposInversiones
    form_class = tiposInversionesForm
    template_name = 'crudsimulador/tipoInversiones_form.html'
    success_url = reverse_lazy('tiposInversiones:tiposInversiones_listar')

class tiposInversionesList(ListView):
    queryset = tiposInversiones.objects.order_by('idtipoInversiones')
    template_name = 'crudsimulador/tipoInversiones_list.html'

class tiposInversionesUpdate(UpdateView):
    model = tiposInversiones
    form_class = tiposInversionesForm
    template_name = 'crudsimulador/tipoInversiones_form.html'
    success_url = reverse_lazy('tiposInversiones:tiposInversiones_listar')

class tiposInversionesDelete(DeleteView):
    model = tiposInversiones
    template_name = 'crudsimulador/tipoInversiones_delete.html'
    success_url = reverse_lazy('tiposInversiones:tiposInversiones_listar')

class tiposInversionesShow(DetailView):
    model = tiposInversiones
    template_name = 'crudsimulador/tipoInversiones_show.html'

def search_ti(request):
    tiposInversiones_list = tiposInversiones.objects.all()
    tiposInversiones_filter = tiposInversionesFilter(request.GET, queryset = tiposInversiones_list)
    return render(request, 'crudsimulador/tipoInversiones_list_filter.html', {'filter': tiposInversiones_filter})