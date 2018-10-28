import django_filters
from apps.crud_simulador.models import perfil_usuario, manoObraComisionesVenta, datos_empresa, manoObra\
    , conceptoCrecimientoDemanda, estimacion_servicios, tipoGastoOperativo, costosTotalesAnuales,tiposGastoss,producto_servicio, gastos, crecimientoDemanda\
    ,tipoUsuario,gastosIndirectos,Usuario, tiposGastos, materiaPrimaInsumos,estimacion_crecimiento_anual,tiposInversiones

#filters de alex:v
class perfilFilter(django_filters.FilterSet):
    class Meta:
        model = perfil_usuario
        fields = ['idperfil', 'nombre_usuario']

class McomisionesVFilter(django_filters.FilterSet):
    class Meta:
        model = manoObraComisionesVenta
        fields = ['idmanoObraComisionesVenta', 'ventas_mensuales']

#filters de luis xD
class datos_empresaFilter(django_filters.FilterSet):
    class Meta:
        model = datos_empresa
        fields =['id_empresa','nombre_empresa']

class manoObraFilter(django_filters.FilterSet):
        class Meta:
            model = manoObra
            fields = ['idManoObra','concepto']

class conceptoCrecimientoDemandaFilter(django_filters.FilterSet):
    class Meta:
        model = conceptoCrecimientoDemanda
        fields = ['idccd']

#Filters de Everardo

class estimacion_serviciosFilter(django_filters.FilterSet):
    class Meta:
        model = estimacion_servicios
        fields = ['id_suscripcion', 'unidad_produccion']

class tipoGastoOperativoFilter(django_filters.FilterSet):
    class Meta:
        model = tipoGastoOperativo
        fields = ['idtipoGasto', 'concepto']

#filters de carmen
class costosFilter(django_filters.FilterSet):
    class Meta:
        model = costosTotalesAnuales
        fields = ['idcostosTotalesAnuales', 'anio']

class gastosFilter(django_filters.FilterSet):
    class Meta:
        model = tiposGastoss
        fields = ['idtiposGastoss', 'concepto']

class productoFilter(django_filters.FilterSet):
    class Meta:
        model = producto_servicio
        fields = ['id_producto', 'producto_nombre']

#Filters de Alan
class gastossFilter(django_filters.FilterSet):
    class Meta:
        model = gastos
        fields = ['unidadMedida']

class crecimientoDemandaFilter(django_filters.FilterSet):
    class Meta:
        model = crecimientoDemanda
        fields = ['crecimiento']

class tipoUsuarioFilter(django_filters.FilterSet):
    class Meta:
        model = tipoUsuario
        fields = ['nombre']

#Filters de Emmanuel
class gastosIndirectosFilter(django_filters.FilterSet):
    class Meta:
        model = gastosIndirectos
        fields = ['idgastosIndirectos', 'concepto']

class usuarioFilter(django_filters.FilterSet):
     class Meta:
         model = Usuario
         fields = ['idusuario', 'usuario']

class tiposGastosFilter(django_filters.FilterSet):
      class Meta:
         model = tiposGastos
         fields = ['idtipoGastos', 'concepto']

#filters de aldair
class materiaPrimaFilter(django_filters.FilterSet):
    class Meta:
        model = materiaPrimaInsumos
        fields = ['idmateriaPrimaInsumos', 'concepto']

class estimacionFilter(django_filters.FilterSet):
     class Meta:
         model = estimacion_crecimiento_anual
         fields = ['numero_anio', 'estimacion']

class tiposInversionesFilter(django_filters.FilterSet):
      class Meta:
         model = tiposInversiones
         fields = ['idtipoInversiones', 'concepto']