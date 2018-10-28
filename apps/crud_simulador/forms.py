from django import forms
from apps.crud_simulador.models import perfil_usuario, manoObraComisionesVenta, datos_empresa, manoObra,conceptoCrecimientoDemanda, estimacion_servicios, tipoGastoOperativo\
    ,costosTotalesAnuales,tiposGastoss,producto_servicio, gastos, crecimientoDemanda\
    ,tipoUsuario,gastosIndirectos,Usuario, tiposGastos, tiposInversiones,estimacion_crecimiento_anual,materiaPrimaInsumos

class perfilusuarioForm(forms.ModelForm):
    class Meta:
        model = perfil_usuario
        fields = [
            'idperfil',
            'nombre_usuario',
            'apellido_p_usuario',
            'apellido_m_usuario',
            'rfc_usuario',
            'email_usuario',
            'telefono_usuario',
            'domicilio_usuario',
            'colonia_usuario',
            'codigo_postal_usuario',
            'ciudad_usuario',
            'estado_usuario',
            'usuario_idusuario'
        ]
        labels = {
            'idperfil': 'Identificacion',
            'nombre_usuario': 'Nombre',
            'apellido_p_usuario': 'Apellido Paterno',
            'apellido_m_usuario': 'Apellido Materno',
            'rfc_usuario': 'RFC Del Usuario',
            'email_usuario': 'Correo Electronico',
            'telefono_usuario': 'Numero De Telefono',
            'domicilio_usuario': 'Direccion',
            'colonia_usuario': 'Colonia',
            'codigo_postal_usuario':'Codigo Postal',
            'ciudad_usuario': 'Ciudad',
            'estado_usuario': 'Estado',
            'usuario_idusuario': 'Usuario'

        }

        widgets = {
            'idperfil': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_p_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_m_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'rfc_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'email_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'colonia_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'codigo_postal_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'estado_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'usuario_idusuario': forms.Select(attrs={'class':'form-control'})

        }

class ManoObraCventaForm(forms.ModelForm):
    class Meta:
        model = manoObraComisionesVenta
        fields = [
            'idmanoObraComisionesVenta',
            'concepto',
            'ventas_mensuales',
            'comision',
            'total_empleados',
            'costo_anual',
            'datos_empresa_id_empresa'
        ]
        labels = {
            'idmanoObraComisionesVenta': 'Id MOCV',
            'concepto': 'Concepto',
            'ventas_mensuales': 'Ventas Mensuales',
            'comision': 'Comision',
            'total_empleados': 'Total Empleados',
            'costo_anual': 'Costo Anual',
            'datos_empresa_id_empresa': 'Id de la empresa'
        }
        widgets = {
            'idmanoObraComisionesVenta': forms.TextInput(attrs={'class': 'form-control'}),
            'concepto': forms.TextInput(attrs={'class': 'form-control'}),
            'ventas_mensuales': forms.TextInput(attrs={'class': 'form-control'}),
            'comision': forms.TextInput(attrs={'class': 'form-control'}),
            'total_empleados': forms.TextInput(attrs={'class': 'form-control'}),
            'costo_anual': forms.TextInput(attrs={'class': 'form-control'}),
            'datos_empresa_id_empresa': forms.Select(attrs={'class': 'form-control'})
        }

#formulario de luis david arenas :v



class datos_empresaForm(forms.ModelForm):
    class Meta:
        model = datos_empresa

        fields =[

            'id_empresa',
            'usuario_idusuario',
            'nombre_empresa',
            'dias_produccion',
            'numero_servicios',
            'no_socios',
            'denominacion_social',
            'rfc',
            'telefono',
            'sitio_web',
            'email',
            'calle_domicilio',
            'codigo_postal',
            'ciudad_empresa',
            'estado_empresa'
        ]
        labels = {
            'id_empresa' : 'id empresa',
            'usuario_idusuario' : 'usarios id',
            'nombre_empresa' : 'nombre de la empresa',
            'dias_produccion' : 'dias de produccion',
            'numero_servicios' : 'numero de servicios',
            'no_socios' : 'numero de socios',
            'denominacion_social': 'denominacion social',
            'rfc' : ' rfc',
            'telefono' : 'telefono',
            'sitio_web' : ' sitio web',
            'email' : 'email',
            'calle_domicilio' : 'calle domicilio',
            'codigo_postal': 'codigo postal',
            'ciudad_empresa' : 'ciudad empresa',
            'estado_empresa' : 'estado empresa'

        }



        widgets = {

            'id_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario_idusuario': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'dias_produccion': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_servicios': forms.TextInput(attrs={'class': 'form-control'}),
            'no_socios': forms.TextInput(attrs={'class': 'form-control'}),
            'denominacion_social': forms.TextInput(attrs={'class': 'form-control'}),
            'rfc': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'sitio_web': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'calle_domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_empresa': forms.TextInput(attrs={'class': 'form-control'}),


        }


class manoObraForm(forms.ModelForm):
    class Meta:
        model = manoObra
        fields = [
        'idManoObra',
        'concepto' ,
        'salario_base',
        'total_empleados',
        'costo_anual' ,
        'datos_empresa_id_empresa'

        ]
        labels = {

        'idManoObra' : 'idManoObra' ,
        'concepto' :  'concepto',
        'salario_base': 'salario_base',
        'total_empleados' : 'total_empleados',
        'costo_anual' : 'costo_anual',
        'datos_empresa_id_empresa':  'datos_empresa_id_empresa'

        }
        widgets = {

        'idManoObra' : forms.TextInput(attrs={'class': 'form-control'}),
        'concepto': forms.TextInput(attrs={'class': 'form-control'}),
        'salario_base' : forms.TextInput(attrs={'class': 'form-control'}),
        'total_empleados' :forms.TextInput(attrs={'class': 'form-control'}),
        'costo_anual' : forms.TextInput(attrs={'class': 'form-control'}),
        'datos_empresa_id_empresa' : forms.TextInput(attrs={'class': 'form-control'}),

        }

class conceptoCrecimientoDemandaForm (forms.ModelForm):
    class Meta:
        model = conceptoCrecimientoDemanda
        fields = [
        'idccd' ,
        'concepto' ,
        'crecimientoInicial'
        ]

        labels = {
            'idccd' :  'idccd',
            'concepto' : 'concepto',
            'crecimientoInicial' : 'crecimientoInicial'
        }

    widgets = {
        'idccd' :  forms.TextInput(attrs={'class': 'form-control'}),
        'concepto' :  forms.TextInput(attrs={'class': 'form-control'}),
        'crecimientoInicial' :  forms.TextInput(attrs={'class': 'form-control'}),
    }

#Formularios de Everardo

class estimacion_serviciosForm(forms.ModelForm):
    class Meta:
        model = estimacion_servicios
        fields = [
            'id_suscripcion',
            'unidad_produccion',
            'total_suscripciones',
            'total_mensual',
            'producto_servicio_id_producto'
        ]
        labels = {
            'id_suscrpcion': 'suscripcion',
            'unidad_produccion': 'unidad de produccion',
            'total_suscripciones': 'total de suscripciones',
            'total_mensual': 'total mensual',
            'producto_servicio_id_producto': 'producto servicio',
        }

        widgets = {
        'id_suscripcion': forms.TextInput(attrs={'class': 'form-control'}),
        'unidad_produccion': forms.TextInput(attrs={'class': 'form-control'}),
        'total_suscripciones': forms.TextInput(attrs={'class': 'form-control'}),
        'total_mensual': forms.TextInput(attrs={'class': 'form-control'}),
        'producto_servicio_id_producto': forms.TextInput(attrs={'class': 'form-control'}),

        }
class  tipoGastoOperativoForms(forms.ModelForm):
     class Meta:
        model = tipoGastoOperativo
        fields = [
            'idtipoGasto',
            'concepto'

        ]
        labels = {
            'idtipoGasto': 'idtipoGasto',
            'concepto': 'concepto'

        }

        widgets = {
        'idtipoGasto': forms.TextInput(attrs={'class': 'form-control'}),
        'concepto': forms.TextInput(attrs={'class': 'form-control'}),

        }
#forms de carmen
class costototalForm(forms.ModelForm):
    class Meta:
        model = costosTotalesAnuales
        fields =[
            'idcostosTotalesAnuales',
            'anio',
            'tiposGastoss',
            'datos_empresa_id_empresa'
        ]
        labels = {
            'idcostosTotalesAnuales': 'Costo Total Anual',
            'anio': 'Anio',
            'tiposGastoss': 'Tipo de Gastos',
            'datos_empresa_id_empresa': 'Datos de Empresa'
        }
        widgets = {
            'idcostosTotalesAnuales': forms.TextInput(attrs={'class':'form-control'}),
            'anio': forms.TextInput(attrs={'class':'datepicker'}),
            'tiposGastoss': forms.Select(attrs={'class':'form-control'}),
            'datos_empresa_id_empresa': forms.Select(attrs={'class':'form-control'})
        }
class tiposgastosForm(forms.ModelForm):
    class Meta:
        model = tiposGastoss
        fields =[
            'idtiposGastoss',
            'concepto'
        ]
        labels ={
            'idtiposGastoss': 'Tipo de Gasto',
            'concepto': 'Cocepto'
        }
        widgets = {
            'idtiposGastoss': forms.TextInput(attrs={'class':'form-control'}),
            'concepto': forms.TextInput(attrs={'class':'form-control'})
        }
class productoSForm(forms.ModelForm):
    class Meta:
        model = producto_servicio
        fields =[
            'id_producto',
            'producto_nombre',
            'unidad_produccion',
            'produccion_mensual',
            'costo_unitario',
            'margen_utilidad',
            'precio_publico',
            'datos_empresa_id_empresa'
        ]
        labels = {
            'id_producto': 'Producto',
            'producto_nombre': 'Nombre del Producto',
            'unidad_produccion': 'Unidad de Produccion',
            'produccion_mensual': 'Poduccion Mensual',
            'costo_unitario': 'Costo Unitario',
            'margen_utilidad': 'Margen Utilidad',
            'precio_publico': 'Precio Publico',
            'datos_empresa_id_empresa': 'Datos de la empesa'
        }
        widgets = {
            'id_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'producto_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad_produccion': forms.TextInput(attrs={'class': 'form-control'}),
            'produccion_mensual': forms.TextInput(attrs={'class': 'form-control'}),
            'costo_unitario': forms.TextInput(attrs={'class': 'form-control'}),
            'margen_utilidad': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_publico': forms.TextInput(attrs={'class': 'form-control'}),
            'datos_empresa_id_empresa': forms.TextInput(attrs={'class': 'form-control'}),
        }
#forms de alan

class gastosForm(forms.ModelForm):
    class Meta:
        model = gastos
        fields = [
            'idgastos',
            'conceptoGastos',
            'unidadMedida',
            'precioUnitario',
            'cantidad',
            'estimacionMensual',
            'estimacionAnual',
            'tiposGastos_idtipoGastos',
            'datos_empresa_id_empresa'
        ]

        labels = {
            'idgastos':'gastos',
            'conceptoGastos':'concepto gastos',
            'unidadMedida':'unidad medida',
            'precioUnitario' :'precio unitario',
            'cantidad':'cantidad',
            'estimacionMensual':'estimacion mensual',
            'estimacionAnual':'estimacion anual',
            'tiposGastos_idtipoGastos': 'tipos gastos',
            'datos_empresa_id_empresa': 'datos empresa'
        }

        widgets = {
            'idgastos': forms.TextInput(attrs={'class':'form-control'}),
            'conceptoGastos': forms.TextInput(attrs={'class':'form-control'}),
            'unidadMedida':forms.TextInput(attrs={'class':'form-control'}),
            'precioUnitario':forms.TextInput(attrs={'class':'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'estimacionMensual': forms.TextInput(attrs={'class': 'form-control'}),
            'estimacionAnual':forms.TextInput(attrs={'class':'form-control'}),
            'tiposGastos_idtipoGastos': forms.Select(attrs={'class': 'form-control'}),
            'datos_empresa_id_empresa':forms.Select(attrs={'class':'form-control'}),
        }


class crecimientoDemandaForm(forms.ModelForm):
    class Meta:
        model = crecimientoDemanda
        fields = [
            'idcrecimientoDemanda',
            'anio',
            'crecimiento',
            'conceptoCrecimientoDemanda_idccd',
            'datos_empresa_id_empresa'

        ]

        labels = {
            'idcrecimientoDemanda': 'crecimiento de demanda',
            'anio': 'anio',
            'crecimiento': 'crecimiento',
            'conceptoCrecimientoDemanda_idccd': 'concepto de crecimiento de damanda',
            'datos_empresa_id_empresa': 'datos de empresa'

        }

        widgets = {
            'idcrecimientoDemanda': forms.TextInput(attrs={'class': 'form-control'}),
            'anio': forms.TextInput(attrs={'class': 'form-control'}),
            'crecimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'conceptoCrecimientoDemanda_idccd': forms.Select(attrs={'class': 'form-control'}),
            'datos_empresa_id_empresa': forms.Select(attrs={'class': 'form-control'}),
        }


class tipoUsuarioForm(forms.ModelForm):
    class Meta:
        model = tipoUsuario
        fields = [
            'idtipoUsuario',
            'nombre',
            'no_empresas'

        ]

        labels = {
            'idtipoUsuario': 'tipo de usuario',
            'nombre': 'nombre',
            'no_empresas': 'no_empresa'

        }

        widgets = {
            'idtipoUsuario': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'no_empresas': forms.TextInput(attrs={'class': 'form-control'}),

        }

#forms de Emmanuel

class gastosIndirectosForm(forms.ModelForm):
   class Meta:
      model = gastosIndirectos
      fields = [
            'idgastosIndirectos',
            'concepto',
            'unidadMedida',
            'precioUnitario',
            'cantidad',
            'estimacionMensual',
            'estimacionAnual',
            'datos_empresa'
      ]
      labels = {
            'idgastosIndirectos':'numero de gastos indirectos',
            'concepto': 'concepto',
            'unidadMedida':'unidad de medida',
            'precioUnitario': 'precio unitario',
            'cantidad':'cantidad',
            'estimacionMensual': 'estimacion mensual',
            'estimacionAnual':'estimacion anual',
            'datos_empresa':'datos empresa'
       }
      widgets={
          'idgastosIndirectos':forms.TextInput(attrs={'class':'forms-control'}),
          'concepto':forms.TextInput(attrs={'class':'forms-control'}),
          'unidadMedida':forms.TextInput(attrs={'class':'forms-control'}),
          'precioUnitario':forms.TextInput(attrs={'class':'forms-control'}),
          'cantidad': forms.TextInput(attrs={'class': 'forms-control'}),
          'estimacionMensual': forms.TextInput(attrs={'class': 'forms-control'}),
          'estimacionAnual': forms.TextInput(attrs={'class': 'forms-control'}),
          'datos_empresa':forms.Select(attrs={'class':'forms-control'}),
      }
class usuarioForm(forms.ModelForm):
   class Meta:
      model = Usuario
      fields = [
            'idusuario',
            'usuario',
            'password',
            'last_access',
            'datos_empresas'
      ]
      labels = {
            'idusuario': 'numero de usuarios',
            'usuario':'usuario',
            'password':'contraseña',
            'last_access':'acceso',
            'datos_empresas':'datos empresa'
       }
      widgets={
          'idusuario':forms.TextInput(attrs={'class':'forms-control'}),
          'usuario':forms.TextInput(attrs={'class':'forms-control'}),
          'password':forms.TextInput(attrs={'class':'forms-control'}),
          'last_access':forms.TextInput(attrs={'class':'forms-control'}),
          'datos_empresas':forms.Select(attrs={'class':'forms-control'}),

      }

class tiposGastosForm(forms.ModelForm):
   class Meta:
      model = tiposGastos
      fields = [
            'idtipoGastos',
            'concepto'

      ]
      labels = {
            'idtipoGastos': 'tipo gastos',
            'concepto': 'concepto'


       }
      widgets={
          'idtipoGastos':forms.TextInput(attrs={'class':'forms-control'}),
          'concepto':forms.Select(attrs={'class':'forms-control'}),

      }

#forms de aldair

class materiaPrimaForm(forms.ModelForm):
   class Meta:
      model = materiaPrimaInsumos
      fields = [
      'idmateriaPrimaInsumos',
      'concepto',
      'unidadMedida',
      'precioUnitario',
      'cantidad',
      'estimacionMensual',
      'estimacionAnual',
      'id_empresa'

      ]
      labels = {
          'idmateriaPrimaInsumos': 'Materia Prima Insumos',
          'concepto': 'Concepto',
          'unidadMedida': 'Unidad Medida',
          'precioUnitario': 'Precio Unitario',
          'cantidad': 'Cantidad',
          'estimacionMensual': 'Estimacion Mensual',
          'estimacionAnual': 'Estimacion Anual',
          'id_empresa': 'id empresa'
      }
      widgets={
          'idmateriaPrimaInsumos':forms.TextInput(attrs={'class':'forms-control'}),
          'concepto':forms.TextInput(attrs={'class':'forms-control'}),
          'unidadMedida':forms.TextInput(attrs={'class':'forms-control'}),
          'precioUnitario':forms.TextInput(attrs={'class':'forms-control'}),
          'cantidad': forms.TextInput(attrs={'class': 'forms-control'}),
          'estimacionMensual': forms.TextInput(attrs={'class': 'forms-control'}),
          'estimacionAnual': forms.TextInput(attrs={'class': 'forms-control'}),
          'id_empresa':forms.Select(attrs={'class':'forms-control'}),
      }
class estimacionForm(forms.ModelForm):
   class Meta:
      model = estimacion_crecimiento_anual
      fields = [
            'numero_anio',
            'estimacion',
            'producto_servicio_id_producto',

      ]
      labels = {
            'numero_anio': 'numero de año',
            'estimacion':'estimacion',
            'producto_servicio_id_producto':'id producto',

       }
      widgets={
          'numero_anio':forms.TextInput(attrs={'class':'forms-control'}),
          'estimacion':forms.TextInput(attrs={'class':'forms-control'}),
          'producto_servicio_id_producto':forms.Select(attrs={'class':'forms-control'}),

      }

class tiposInversionesForm(forms.ModelForm):
   class Meta:
      model = tiposInversiones
      fields = [
            'idtipoInversiones',
            'concepto'

      ]
      labels = {
            'idtipoInversiones': 'tipo inversiones',
            'concepto': 'concepto'


       }
      widgets={
          'idtipoInversiones':forms.TextInput(attrs={'class':'forms-control'}),
          'concepto':forms.TextInput(attrs={'class':'forms-control'}),

      }

