from django.shortcuts import render,  redirect

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from core.models import Modulo, ResAprendizaje, CritEvaluacion
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from core.mixins import coreMixin, deleteMixin
from core.forms import ModuloForm, ResAprendizajeForm, CritEvaluacionForm
from django.contrib.messages.views import SuccessMessageMixin

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

class ModuloListView(ListView):
    model = Modulo
    template_name = 'core/modulo_list.html'
    # UD6.8.a
    paginate_by = 10

    #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    #UD7.2.j
    def get_queryset(self):
        orden = self.request.GET.get('orden', None)
        queryset = Modulo.objects.all()
        if orden:
            if orden == 'asc':
                queryset = queryset.order_by('id')
            elif orden == 'desc':
                queryset = queryset.order_by('-id')

        return queryset


class ModuloDetailView(DetailView):
    model = Modulo
    template_name = 'core/modulo_detail.html'

    #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



class RAListView(ListView):
    model = ResAprendizaje
    template_name = 'core/ra_list.html'
     # UD6.8.a
    paginate_by = 10

    #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    #UD7.2.j
    def get_queryset(self):
        orden = self.request.GET.get('orden', None)
        queryset = ResAprendizaje.objects.all()
        if orden:
            if orden == 'asc':
                queryset = queryset.order_by('id')
            elif orden == 'desc':
                queryset = queryset.order_by('-id')

        return queryset



class RADetailView(DetailView):
    model = ResAprendizaje
    template_name = 'core/ra_detail.html'

    #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



class CEListView(ListView):
    model = CritEvaluacion
    template_name = 'core/ce_list.html'
     # UD6.8.a
    paginate_by = 10

    #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #UD7.2.j
    def get_queryset(self):
        orden = self.request.GET.get('orden', None)
        queryset = CritEvaluacion.objects.all()
        if orden:
            if orden == 'asc':
                queryset = queryset.order_by('id')
            elif orden == 'desc':
                queryset = queryset.order_by('-id')

        return queryset



class CEDetailView(DetailView):
    model = CritEvaluacion
    template_name = 'core/ce_detail.html'

    #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    
#UD7.2.a
class ModCreateView(coreMixin, SuccessMessageMixin,  CreateView):
    model= Modulo
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('modulo_update')
    
    #UD7.2.c
    titulo_actualizacion = ''
    titulo_creacion = 'crear un modulo'
    url_borrado = 'modulo_delete'

    form_class = ModuloForm

    #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_success_message(self, cleaned_data):
        return "Modulo '{}' creado exitosamente".format(str(self.object))

    def get_success_url(self):
        object = self.object
        return reverse_lazy('modulo_update', kwargs={'pk': object.id})

#UD7.2.a
class ModUpdateView(SuccessMessageMixin, coreMixin, UpdateView):
    model= Modulo
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('modulo_update')
    
    #UD7.2.c
    #UD7.2.c
    titulo_actualizacion = 'actualizar un módulo'
    titulo_creacion = ''
    url_borrado = 'modulo_delete'

    form_class = ModuloForm

    #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_success_message(self, cleaned_data):
        return "Modulo '{}' actualizado exitosamente".format(str(self.object))

    def get_success_url(self):
        object = self.object
        return reverse_lazy('modulo_update', kwargs={'pk': object.id})

#UD7.2.a
class ModDeleteView(deleteMixin, DeleteView):
    model= Modulo
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('modulo_list')
    #UD7.2.f
    titulo = 'Modulo'
    mensaje_confirmacion = '¿Estas seguro de que quieres borrar el modulo?'
    
    #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

        
#UD7.2.a
class RACreateView(SuccessMessageMixin , coreMixin, CreateView):
    model= ResAprendizaje
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('ra_update')
    #UD7.2.c
    titulo_actualizacion = ''
    titulo_creacion = 'crear un resultado de aprendizaje'
    url_borrado = 'ra_delete'

    form_class = ResAprendizajeForm

    #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_message(self, cleaned_data):
        return "RA '{}' creado exitosamente".format(str(self.object))
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('ra_update', kwargs={'pk': object.id})

#UD7.2.a
class RAUpdateView(SuccessMessageMixin , coreMixin, UpdateView):
    model= ResAprendizaje
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('ra_update')
    #UD7.2.c
    titulo_actualizacion = 'actualizar un resultado aprendizaje'
    titulo_creacion = ''
    url_borrado = 'ra_delete'

    #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    form_class = ResAprendizajeForm

    def get_success_message(self, cleaned_data):
        return "RA '{}' actualizado exitosamente".format(str(self.object))
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('ra_update', kwargs={'pk': object.id})

#UD7.2.a
class RADeleteView(deleteMixin, DeleteView):
    model= ResAprendizaje
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('ra_list')
    #UD7.2.f
    titulo = 'Resultado aprendizaje'
    mensaje_confirmacion = '¿Estas seguro de que quieres borrar el resultado de aprendizaje?'
    
    #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
#UD7.2.a
class CECreateView(SuccessMessageMixin , coreMixin, CreateView):
    model= CritEvaluacion
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('ce_update')
    #UD7.2.c
    titulo_actualizacion = ''
    titulo_creacion = 'crear un criterio de evaluación'
    url_borrado = 'ce_delete'

    
    form_class = CritEvaluacionForm

    #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_success_message(self, cleaned_data):
        return "CE '{}' creado exitosamente".format(str(self.object))
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('ce_update', kwargs={'pk': object.id})

#UD7.2.a
class CEUpdateView(SuccessMessageMixin , coreMixin, UpdateView):
    model = CritEvaluacion
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('ce_update')
    #UD7.2.c
    titulo_actualizacion = 'actualizar un criterio evaluación'
    titulo_creacion = ''
    url_borrado = 'ce_delete'
    

    form_class = CritEvaluacionForm

    #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_message(self, cleaned_data):
        return "CE '{}' actualizado exitosamente".format(str(self.object))
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('ce_update', kwargs={'pk': object.id})

#UD7.2.a
class CEDeleteView(deleteMixin, DeleteView):
    model = CritEvaluacion
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('ce_list')
    #UD7.2.f
    titulo = 'Criterio de evaluación' 
    mensaje_confirmacion = '¿Estas seguro de que quieres eliminar el criterio de evaluacion?'

   #UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    