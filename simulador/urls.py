"""simulador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include


urlpatterns = [
    url(r'^perfil/', include(('apps.crud_simulador.urls', 'apps'), namespace='perfil_usuario')),
    url(r'^mcomisiones/', include(('apps.crud_simulador.urls', 'apps'), namespace='mcomisiones')),

    #urls de luis xD
    url(r'^datos_empresa/',include(('apps.crud_simulador.urls', 'apps'), namespace='datos_empresa')),
    url(r'^manoObra/',include(('apps.crud_simulador.urls', 'apps'), namespace='manoObra')),
    url(r'^demanda/',include(('apps.crud_simulador.urls', 'apps'), namespace='demanda')),

    #urls de Ever xD
    url(r'^estimacion_servicios/', include(('apps.crud_simulador.urls', 'apps'), namespace='estimacion_servicios')),
    url(r'^tipoGastoOperativo/', include(('apps.crud_simulador.urls', 'apps'), namespace='tipoGastoOperativo')),

 #urls de carmen
    url(r'^costos/', include(('apps.crud_simulador.urls', 'apps'), namespace='costos')),
    url(r'^gastos/', include(('apps.crud_simulador.urls', 'apps'), namespace='gastos')),
    url(r'^producto/', include(('apps.crud_simulador.urls', 'apps'), namespace='producto')),
   #Urls de Alan
    url(r'^gastoss/',include(('apps.crud_simulador.urls','apps',),namespace='gastoss')),
    url(r'^crecimientoDemanda/', include(('apps.crud_simulador.urls', 'apps',), namespace='crecimientoDemanda')),
    url(r'^tipoUsuario/', include(('apps.crud_simulador.urls', 'apps',), namespace='tipoUsuario')),

#urls de Emmanuel

    url(r'^gastosIndirectos/', include(('apps.crud_simulador.urls', 'apps'), namespace='gastosIndirectos')),
    url(r'^usuario/', include(('apps.crud_simulador.urls', 'apps'), namespace='usuario')),
    url(r'^tiposGastos/', include(('apps.crud_simulador.urls', 'apps'), namespace='tiposGastos')),

#urls de aldair
    url(r'^tiposInversiones/', include(('apps.crud_simulador.urls', 'apps'), namespace='tiposInversiones')),
    url(r'^materiaPrima/', include(('apps.crud_simulador.urls', 'apps'), namespace='materiaPrima')),
    url(r'^estimacion/', include(('apps.crud_simulador.urls', 'apps'), namespace='estimacion')),
]
