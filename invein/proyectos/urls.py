from django.urls import path
from . import views

urlpatterns = [
    path('crear_comercial/', views.CrearComercial.as_view(), name='crear_comercial'),
    path('listado_comerciales/', views.ListadoComercial.as_view(), name='listado_comercial'),
    path('editar_comercial/<pk>/', views.EditarComercial.as_view(), name='editar_comercial'),
    path('borrar_comercial/<pk>/', views.BorrarComecial.as_view(), name='borrar_comercial'),

    path('crear_cliente/', views.CrearCliente.as_view(), name='crear_cliente'),
    path('listado_clientes/', views.ListadoCliente.as_view(), name='listado_cliente'),
    path('editar_cliente/<pk>/', views.EditarCliente.as_view(), name='editar_cliente'),
    path('borrar_cliente/<pk>/', views.BorrarCliente.as_view(), name='borrar_cliente'),

    path('crear_oferta/', views.CrearOferta.as_view(), name='crear_oferta'),
    path('listado_oferta/', views.ListadoOferta.as_view(), name='listado_oferta'),
    path('editar_oferta/<pk>/', views.EditarOferta.as_view(), name='editar_oferta'),
    path('borrar_oferta/<pk>/', views.BorrarOferta.as_view(), name='borrar_oferta'),

    path('crear_montaje/', views.CrearMontaje.as_view(), name='crear_montaje'),
    path('listado_montaje/', views.ListadoMontaje.as_view(), name='listado_montaje'),
    path('editar_montaje/<pk>/', views.EditarMontaje.as_view(), name='editar_montaje'),
    path('borrar_montaje/<pk>/', views.BorrarMontaje.as_view(), name='borrar_montaje'),
    path('detalle_montaje/<int:id>/', views.detalle_montaje, name='detalle_montaje'),

    path('crear_fabricacion/', views.CrearFabricacion.as_view(), name='crear_fabricacion'),
    path('listado_fabricacion/', views.ListadoFabricacion.as_view(), name='listado_fabricacion'),
    path('editar_fabricacion/<pk>/', views.EditarFabricacion.as_view(), name='editar_fabricacion'),
    path('borrar_fabricacion/<pk>/', views.BorrarFabricacion.as_view(), name='borrar_fabricacion'),
    path('detalle_fabricacion/<int:id>/', views.detalle_fabricacion, name='detalle_fabricacion'),
    

    path('crear_proyecto/', views.CrearProyecto.as_view(), name='crear_proyecto'),
    path('listado_proyecto/', views.ListadoProyecto.as_view(), name='listado_proyecto'),
    path('editar_proyecto/<pk>/', views.EditarProyecto.as_view(), name='editar_proyecto'),
    path('borrar_proyecto/<pk>/', views.BorrarProyecto.as_view(), name='borrar_proyecto'),
    path('detalle_proyecto/<int:id>/', views.detalle_proyecto, name='detalle_proyecto'),

    path('crear_actividad/', views.CrearActividad.as_view(), name='crear_actividad'),
    path('detalle_actividad/<int:id>/', views.detalle_actividad, name='detalle_actividad'),
    path('actualizar_actividad/<int:id>/', views.editar_actividad, name='actualizar_actividad'),
    path('eliminar_actividad/<pk>/', views.BorrarActividad.as_view(), name='borrar_actividad'),

    path('puntos_curva/<int:id>/', views.lista_puntos, name="puntos"),
    path('editar_punto/<int:id>/', views.editar_curva, name="editar_curva"),
]