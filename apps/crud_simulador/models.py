from django.db import models

# Create your models here.
class tipoUsuario(models.Model):
    idtipoUsuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    no_empresas = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.nombre)

class tiposInversiones(models.Model):
    idtipoInversiones = models.IntegerField(primary_key=True)
    concepto = models.CharField(max_length=85)

    def __str__(self):
        return '{}'.format(self.concepto)

class tiposGastos(models.Model):
    idtipoGastos = models.IntegerField(primary_key=True)
    concepto = models.CharField(max_length=85)

    def __str__(self):
        return '{}'.format(self.concepto)

class tiposGastoss(models.Model):
    idtiposGastoss = models.IntegerField(primary_key=True)
    concepto = models.CharField(max_length=85)

    def __str__(self):
        return '{}'.format(self.concepto)

class conceptoCrecimientoDemanda(models.Model):
    idccd = models.IntegerField(primary_key=True)
    concepto = models.CharField(max_length=85)
    crecimientoInicial = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.concepto)

class tipoGastoOperativo(models.Model):
    idtipoGasto = models.IntegerField(primary_key=True)
    concepto = models.CharField(max_length=45)

    def __str__(self):
        return '{}'.format(self.concepto)

class Usuario(models.Model):
    idusuario = models.BigIntegerField(primary_key=True)
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    last_access = models.DateField()
    datos_empresas = models.ForeignKey(tipoUsuario, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.usuario)

class datos_empresa (models.Model):
    id_empresa = models.IntegerField(primary_key=True)
    nombre_empresa = models.CharField(max_length=85)
    dias_produccion = models.IntegerField()
    numero_servicios = models.IntegerField()
    no_socios = models.IntegerField()
    denominacion_social = models.CharField(max_length=105)
    rfc = models.CharField(max_length=13)
    telefono = models.CharField(max_length=12)
    sitio_web = models.CharField(max_length=85)
    email = models.CharField(max_length=85)
    calle_domicilio = models.CharField(max_length=45)
    codigo_postal = models.CharField(max_length=6)
    ciudad_empresa = models.CharField(max_length=90)
    estado_empresa = models.CharField(max_length=85)
    usuario_idusuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre_empresa)

class producto_servicio(models.Model):
    id_producto = models.IntegerField(primary_key =True)
    producto_nombre = models.CharField(max_length=65)
    unidad_produccion = models.CharField(max_length=45)
    produccion_mensual = models.IntegerField()
    costo_unitario = models.DecimalField(max_digits=5, decimal_places=2)
    margen_utilidad = models.DecimalField(max_digits=5, decimal_places=2)
    precio_publico = models.DecimalField(max_digits=5, decimal_places=2)
    datos_empresa_id_empresa = models.ForeignKey(datos_empresa, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.producto_nombre)

class estimacion_servicios(models.Model):
    id_suscripcion = models.BigIntegerField(primary_key=True)
    unidad_produccion = models.CharField(max_length=100)
    total_suscripciones = models.IntegerField()
    total_mensual = models.DecimalField(max_digits=15, decimal_places=2)
    producto_servicio_id_producto = models.ForeignKey(producto_servicio, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.unidad_produccion)

class estimacion_crecimiento_anual(models.Model):
    numero_anio = models.IntegerField()
    estimacion = models.DecimalField(max_digits=5, decimal_places=2)
    producto_servicio_id_producto = models.ForeignKey(producto_servicio, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.estimacion)

class manoObra (models.Model):
    idManoObra = models.IntegerField(primary_key=True)
    concepto = models.CharField(max_length=85)
    salario_base = models.DecimalField(max_digits=15, decimal_places=2)
    total_empleados = models.IntegerField()
    costo_anual = models.DecimalField(max_digits=15, decimal_places=2)
    datos_empresa_id_empresa = models.ForeignKey(datos_empresa, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.concepto)

class manoObraComisionesVenta(models.Model):
    idmanoObraComisionesVenta = models.IntegerField(primary_key=True)
    concepto = models.CharField(max_length=85)
    ventas_mensuales = models.DecimalField(max_digits=10, decimal_places=2)
    comision = models.DecimalField(max_digits=5, decimal_places=2)
    total_empleados = models.IntegerField()
    costo_anual = models.DecimalField(max_digits=15, decimal_places=2)
    datos_empresa_id_empresa = models.ForeignKey(datos_empresa, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.concepto)

class gastosOperativos(models.Model):
    idgastosOperativos = models.IntegerField(primary_key=True)
    concepto = models.CharField(max_length=85)
    estimacionMensual = models.DecimalField(max_digits=15, decimal_places=2)
    estimacionAnual = models.DecimalField(max_digits=15, decimal_places=2)
    idtipoGasto = models.ForeignKey(datos_empresa, null=True, on_delete=models.CASCADE)
    datos_empresa_id_empresa = models.ForeignKey(tipoGastoOperativo, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.concepto)

class manoObraOperativa(models.Model):
    idmanoObraOperativa = models.IntegerField(primary_key=True)
    concepto = models.CharField(max_length=85)
    unidadMedida = models.CharField(max_length=85)
    precioUnitario = models.DecimalField(max_digits=15, decimal_places=2)
    cantidad = models.IntegerField()
    estimacionMensual = models.DecimalField(max_digits=15, decimal_places=2)
    servicio_id_producto = models.ForeignKey(producto_servicio, null=True, blank=True, on_delete=models.CASCADE)
    datos_empresa_id_empresa = models.ForeignKey(datos_empresa, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.concepto)

class gastos(models.Model):
    idgastos=models.IntegerField(primary_key=True)
    conceptoGastos=models.CharField(max_length=85)
    unidadMedida=models.CharField(max_length=48)
    precioUnitario=models.DecimalField(max_digits=15, decimal_places=2)
    cantidad=models.IntegerField()
    estimacionMensual=models.DecimalField(max_digits=15, decimal_places=2)
    estimacionAnual=models.DecimalField(max_digits=15, decimal_places=2)
    tiposGastos_idtipoGastos=models.ForeignKey(tiposGastos, null=True, blank=True, on_delete=models.CASCADE)
    datos_empresa_id_empresa=models.ForeignKey(datos_empresa, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.conceptoGastos)

class costosTotalesAnuales(models.Model):
    idcostosTotalesAnuales = models.IntegerField(primary_key=True)
    anio = models.DecimalField(max_digits=5, decimal_places=2)
    tiposGastoss = models.ForeignKey(tiposGastoss, null=True, on_delete=models.CASCADE)
    datos_empresa_id_empresa = models.ForeignKey(datos_empresa, null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.idcostosTotalesAnuales)

class crecimientoDemanda(models.Model):
    idcrecimientoDemanda = models.IntegerField(primary_key=True)
    anio = models.IntegerField()
    crecimiento = models.DecimalField(max_digits=5, decimal_places=2)
    conceptoCrecimientoDemanda_idccd = models.ForeignKey(conceptoCrecimientoDemanda, null=True, on_delete=models.CASCADE)
    datos_empresa_id_empresa = models.ForeignKey(datos_empresa, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.idcrecimientoDemanda)

class inversiones(models.Model):
    idinversiones = models.IntegerField(primary_key=True)
    concepto = models.CharField(max_length=85)
    unidad_medida = models.CharField(max_length=85)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=15, decimal_places=2)
    subtotal_1 = models.DecimalField(max_digits=15, decimal_places=2)
    aportacion_propio = models.DecimalField(max_digits=15, decimal_places=2)
    aportacion_financiacion = models.DecimalField(max_digits=15, decimal_places=2)
    subtotal_2 = models.DecimalField(max_digits=15, decimal_places=2)
    depreciacion_amortizacion = models.IntegerField
    tiposInversiones_idtipoInversiones = models.ForeignKey(tiposInversiones, null=True, on_delete=models.CASCADE)
    datos_empresa_id_empresa = models.ForeignKey(datos_empresa, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.concepto)

class perfil_usuario(models.Model):
    idperfil = models.IntegerField(primary_key=True)
    nombre_usuario = models.CharField(max_length=85)
    apellido_p_usuario = models.CharField(max_length=85)
    apellido_m_usuario = models.CharField(max_length=85)
    rfc_usuario = models.CharField(max_length=12)
    email_usuario = models.CharField(max_length=85)
    telefono_usuario = models.CharField(max_length=85)
    domicilio_usuario = models.CharField(max_length=110)
    colonia_usuario=models.CharField(max_length=85)
    codigo_postal_usuario = models.CharField(max_length=6)
    ciudad_usuario = models.CharField(max_length=90)
    estado_usuario = models.CharField(max_length=85)
    usuario_idusuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre_usuario)


class materiaPrimaInsumos(models.Model):
    idmateriaPrimaInsumos = models.IntegerField(primary_key=True)
    concepto = models.CharField(max_length=85)
    unidadMedida = models.CharField(max_length=85)
    precioUnitario = models.DecimalField(max_digits=15, decimal_places=2)
    cantidad = models.IntegerField()
    estimacionMensual = models.DecimalField(max_digits=15, decimal_places=2)
    estimacionAnual = models.DecimalField(max_digits=15, decimal_places=2)
    id_empresa = models.ForeignKey(datos_empresa, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.concepto)

class gastosIndirectos(models.Model):
    idgastosIndirectos = models.IntegerField(primary_key=True)
    concepto = models.CharField(max_length=100)
    unidadMedida = models.CharField(max_length=100)
    precioUnitario = models.DecimalField(max_digits=15, decimal_places=2)
    cantidad = models.IntegerField()
    estimacionMensual = models.DecimalField(max_digits=15, decimal_places=2)
    estimacionAnual = models.DecimalField(max_digits=15, decimal_places=2)
    datos_empresa = models.ForeignKey(datos_empresa, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.concepto)