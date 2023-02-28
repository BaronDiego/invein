
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from core.views import SinPrivilegios
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Comercial, Cliente, Oferta, Proyecto, Fabricacion, Montaje, Actividad, Comentarios, CurvaS
from .forms import ComercialForm, ClienteForm, OfertaForm, ProyectoForm, FabricacionForm, MontajeForm, ActividadForm, ComentarioForm, CurvaForm

# Create your views here.

#Vistas Comercial
class CrearComercial(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "proyectos.add_comercial"
    model = Comercial
    template_name = 'proyectos/comercial/crear_comercial.html'
    form_class = ComercialForm
    success_url = reverse_lazy('listado_comercial')
    success_message = "Comercial creado correctamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ListadoComercial(SinPrivilegios, ListView):
    permission_required = 'proyectos.view_comercial'
    model = Comercial
    template_name = 'proyectos/comercial/listado_comercial.html'
    context_object_name = 'obj'


class EditarComercial(SuccessMessageMixin, SinPrivilegios, UpdateView):
    permission_required = 'proyectos.change_comercial'
    model = Comercial
    form_class = ComercialForm
    context_object_name = 'comercial_editar'
    template_name = 'proyectos/comercial/editar_comercial.html'
    success_url = reverse_lazy('listado_comercial')
    success_message = 'Comercial editado correctamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class BorrarComecial( SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = "proyectos.delete_comercial"
    model = Comercial
    template_name = 'proyectos/comercial/borrar_comercial.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('listado_comercial')
    success_message = "Comercial elimiando satisfactoriamente"


#Vistas Cliente
class CrearCliente(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "proyectos.add_cliente"
    model = Cliente
    template_name = 'proyectos/cliente/crear_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('listado_cliente')
    success_message = "Cliente creado correctamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class ListadoCliente(SinPrivilegios, ListView):
    permission_required = 'proyectos.view_cliente'
    model = Cliente
    template_name = 'proyectos/cliente/listado_cliente.html'
    context_object_name = 'obj'


class EditarCliente(SuccessMessageMixin, SinPrivilegios, UpdateView):
    permission_required = 'proyectos.change_cliente'
    model = Cliente
    form_class = ClienteForm
    context_object_name = 'cliente_editar'
    template_name = 'proyectos/cliente/editar_cliente.html'
    success_url = reverse_lazy('listado_cliente')
    success_message = 'Cliente editado correctamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    

class BorrarCliente( SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = "proyectos.delete_cliente"
    model = Cliente
    template_name = 'proyectos/cliente/borrar_cliente.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('listado_cliente')
    success_message = "Cliente elimiando satisfactoriamente"


#Oferta
class CrearOferta(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "proyectos.add_oferta"
    model = Oferta
    template_name = 'proyectos/oferta/crear_oferta.html'
    form_class = OfertaForm
    success_url = reverse_lazy('listado_oferta')
    success_message = "Oferta creada correctamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class ListadoOferta(SinPrivilegios, ListView):
    permission_required = 'proyectos.view_oferta'
    model = Oferta
    template_name = 'proyectos/oferta/listado_oferta.html'
    context_object_name = 'obj'

class EditarOferta(SuccessMessageMixin, SinPrivilegios, UpdateView):
    permission_required = 'proyectos.change_oferta'
    model = Oferta
    form_class = OfertaForm
    context_object_name = 'cliente_editar'
    template_name = 'proyectos/oferta/editar_oferta.html'
    success_url = reverse_lazy('listado_oferta')
    success_message = 'Oferta editada correctamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class BorrarOferta( SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = "proyectos.delete_oferta"
    model = Oferta
    template_name = 'proyectos/oferta/borrar_oferta.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('listado_oferta')
    success_message = "Oferta elimianda satisfactoriamente"


#Montaje
class CrearMontaje(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "proyectos.add_montaje"
    model = Montaje
    template_name = 'proyectos/montaje/crear_montaje.html'
    form_class = MontajeForm
    success_url = reverse_lazy('listado_montaje')
    success_message = "Montaje creado correctamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class ListadoMontaje(SinPrivilegios, ListView):
    permission_required = 'proyectos.view_montaje'
    model = Montaje
    template_name = 'proyectos/montaje/listado_montaje.html'
    context_object_name = 'obj'

class EditarMontaje(SuccessMessageMixin, SinPrivilegios, UpdateView):
    permission_required = 'proyectos.change_montaje'
    model = Montaje
    form_class = MontajeForm
    context_object_name = 'cliente_editar'
    template_name = 'proyectos/montaje/editar_montaje.html'
    success_url = reverse_lazy('listado_montaje')
    success_message = 'Montaje editado correctamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class BorrarMontaje( SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = "proyectos.delete_montaje"
    model = Montaje
    template_name = 'proyectos/montaje/borrar_montaje.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('listado_montaje')
    success_message = "Montaje elimiando satisfactoriamente"


def detalle_montaje(request, id):
    montaje = get_object_or_404(Montaje, id=id)
    nombre = montaje.numero_orden

    return render(request, 'proyectos/montaje/detalle_montaje.html',
                  {
                    'montaje':montaje,
                    'nombre':nombre
        
                  }
                  )


#Fabricacion
class CrearFabricacion(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "proyectos.add_fabricacion"
    model = Fabricacion
    template_name = 'proyectos/fabricacion/crear_fabricacion.html'
    form_class = FabricacionForm
    success_url = reverse_lazy('listado_fabricacion')
    success_message = "Fabricación creado correctamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class ListadoFabricacion(SinPrivilegios, ListView):
    permission_required = 'proyectos.view_fabricacion'
    model = Fabricacion
    template_name = 'proyectos/fabricacion/listado_fabricacion.html'
    context_object_name = 'obj'

class EditarFabricacion(SuccessMessageMixin, SinPrivilegios, UpdateView):
    permission_required = 'proyectos.change_fabricacion'
    model = Fabricacion
    form_class = FabricacionForm
    context_object_name = 'obj'
    template_name = 'proyectos/fabricacion/editar_fabricacion.html'
    success_url = reverse_lazy('listado_fabricacion')
    success_message = 'Fabricación editado correctamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class BorrarFabricacion( SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = "proyectos.delete_fabricacion"
    model = Fabricacion
    template_name = 'proyectos/fabricacion/borrar_fabricacion.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('listado_fabricacion')
    success_message = "Fabricación elimiando satisfactoriamente"


def detalle_fabricacion(request, id):
    fabricacion = get_object_or_404(Fabricacion, id=id)
    nombre = fabricacion.numero_orden

    return render(request, 'proyectos/fabricacion/detalle_fabricacion.html',
                  {
                    'fabricacion':fabricacion,
                    'nombre':nombre
        
                  }
                  )


#Proyecto
class CrearProyecto(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "proyectos.add_proyecto"
    model = Proyecto
    template_name = 'proyectos/proyecto/crear_proyecto.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('listado_proyecto')
    success_message = "Proyecto creado correctamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class ListadoProyecto(SinPrivilegios, ListView):
    permission_required = 'proyectos.view_proyecto'
    model = Proyecto
    template_name = 'proyectos/proyecto/listado_proyecto.html'
    context_object_name = 'obj'

class EditarProyecto(SuccessMessageMixin, SinPrivilegios, UpdateView):
    permission_required = 'proyectos.change_proyecto'
    model = Proyecto
    form_class = ProyectoForm
    context_object_name = 'obj'
    template_name = 'proyectos/proyecto/editar_proyecto.html'
    success_url = reverse_lazy('listado_proyecto')
    success_message = 'Proyecto editado correctamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class BorrarProyecto( SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = "proyectos.delete_proyecto"
    model = Proyecto
    template_name = 'proyectos/proyecto/borrar_proyecto.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('listado_proyecto')
    success_message = "Proyecto elimiando satisfactoriamente"


@login_required(login_url='login')
def detalle_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    nombre = proyecto.nombre
    comentarios = proyecto.comentarios.filter(activo=True)
    nuevo_comenatrio = None

    #### Crear Cometarios ####
    if request.method == 'POST':
        comentario_form = ComentarioForm(data=request.POST)
        if comentario_form.is_valid():
            nuevo_comenatrio = comentario_form.save(commit=False)
            nuevo_comenatrio.proyecto =proyecto
            comentario_form.instance.uc = request.user
            nuevo_comenatrio.save()
            messages.success(request, 'Comentario creado correctamente')
            return redirect('detalle_proyecto', id=id)
    else:
        comentario_form = ComentarioForm()

    ### Crear Actividades ### 
    if request.method == 'POST':
        form_actividad = ActividadForm(data=request.POST)
        if form_actividad.is_valid():
            cd = form_actividad.cleaned_data
            nueva_actividad = form_actividad.save(commit=False)
            nueva_actividad.proyecto = proyecto
            nueva_actividad.proyecto.um = request.user.id
            form_actividad.instance.uc = request.user
            nueva_actividad.proyecto.save()
            nueva_actividad.save()
            messages.success(request, 'Actividad creada correctamente')
            return redirect('detalle_proyecto', id=id)
    else:
        form_actividad = ActividadForm()


     ### Crear Curva ###
    if request.method == 'POST':
        form_curva = CurvaForm(data=request.POST)
        if form_curva.is_valid():
            cd = form_curva.cleaned_data
            nueva_c = form_curva.save(commit=False)
            nueva_c.proyecto = proyecto
            nueva_c.proyecto.um = request.user.id
            form_curva.instance.uc = request.user
            nueva_c.proyecto.save()
            nueva_c.save()
            return redirect('detalle_proyecto', id=id)
    else:
        form_curva = CurvaForm()

    fechas =[]
    fechas1 = []
    lista_fechas_flat=[]
    programado = []
    programado_list_flat = []
    ejecutado = []
    ejecutado_list_flat = []
    for f in CurvaS.objects.filter(proyecto_id=id).values_list('fecha'):
        fechas.append(f)
    fechas_list = list(map(list,fechas))

    for i in fechas_list:
        lista_fechas_flat += i

    for f in lista_fechas_flat:
        fechas1.append(f.isoformat())

    for p in CurvaS.objects.filter(proyecto_id=id).values_list('programado'):
        programado.append(p)
    programado_list = list(map(list, programado))
    
    for i in programado_list:
        programado_list_flat += i

    for e in CurvaS.objects.filter(proyecto_id=id).values_list('avance'):
        if e != (0.1,):
            ejecutado.append(e)

    ejecutado_list = list(map(list, ejecutado))
    
    for i in ejecutado_list:
        ejecutado_list_flat += i

    actividades = Actividad.objects.filter(proyecto_id=id)

    return render(request, 'proyectos/proyecto/detalle_proyecto.html',
                  {
                    'nombre':nombre,
                    'proyecto':proyecto,
                    'comentarios':comentarios,
                    'nuevo_comentario':nuevo_comenatrio,
                    'comentario_form':comentario_form,
                    'form_actividad':form_actividad,
                    'actividades':actividades,
                    'form_curva':form_curva,
                    'programado_list_flat':programado_list_flat,
                    'fechas1':fechas1,
                    'ejecutado_list_flat':ejecutado_list_flat,
        
                  })




@login_required(login_url='login')
def panel(request):

    proyectos = Proyecto.objects.all()
    fabricaciones = Fabricacion.objects.all()
    montajes = Montaje.objects.all()

    return render(request, 'proyectos/panel.html', {
        'proyectos':proyectos,
        'fabricaciones': fabricaciones,
        'montajes': montajes
        })


class CrearActividad(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "proyectos.add_actividad"
    model = Actividad
    template_name = 'proyectos/actividad/crear_actividad.html'
    form_class = ActividadForm
    success_url = reverse_lazy('graficos')
    success_message = 'Actividad creada correctamente'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


@login_required(login_url='login')
def detalle_actividad(request, id):
    actividades = Actividad.objects.filter(proyecto_id=id)
    try:
        e = Actividad.objects.get(id=id)
    except Actividad.DoesNotExist:
        e = None
    if e == None:
        vp = Proyecto.objects.get(id=id)
    else:
        vp = Proyecto.objects.get(id=e.id)
    return render(request, 'proyectos/actividad/actividad_detalle.html', {'actividades': actividades, 'vp':vp})


@login_required(login_url='login')
@permission_required('proyectos.change_actividad', login_url='sin_privilegios')
def editar_actividad(request, id):
    actividad = get_object_or_404(Actividad, pk=id)
    id_proyecto = actividad.proyecto.id
    if request.method == 'POST':
        form_actividad = ActividadForm(request.POST, instance=actividad)
        if form_actividad.is_valid():
            actividad.um = request.user.id
            form_actividad.save()
            messages.success(request, 'Actividad editada correctamente')
            return redirect('detalle_proyecto', id=id_proyecto)
    else:
        form_actividad = ActividadForm(instance=actividad)
        return render(request, 'proyectos/actividad/actualizar_actividad.html', {'form_actividad':form_actividad})



class BorrarActividad(SuccessMessageMixin, SinPrivilegios, DeleteView):
    permission_required = "proyectos.delete_actividad"
    model = Actividad
    context_object_name = 'obj'
    template_name = 'proyectos/actividad/borrar_actividad.html'
    success_url = reverse_lazy('panel')
    success_message = 'Actividad borrada correctamente'


@login_required(login_url='login')
@permission_required('proyectos.change_curva_s', login_url='sin_privilegios')
def editar_curva(request,id):
    curva = get_object_or_404(CurvaS, pk=id)
    proyecto_id = curva.proyecto.id
    if request.method == 'POST':
        form_curva = CurvaForm(request.POST, instance=curva)
        if form_curva.is_valid():
            curva.um = request.user.id
            form_curva.save()
            messages.success(request, 'curva editada correctamente')
            return redirect('detalle_proyecto', id=proyecto_id)
    else:
        form_curva = CurvaForm(instance=curva)
        return render(request, 'proyectos/curva/editar_curva.html', {'form_curva':form_curva})


@login_required(login_url='login')
@permission_required('proyectos.view_curva_s', login_url='sin_privilegios')
def lista_puntos(request, id):
    puntos = CurvaS.objects.filter(proyecto_id=id)
    return render(request, 'proyectos/curva/lista_puntos.html', {'puntos':puntos})