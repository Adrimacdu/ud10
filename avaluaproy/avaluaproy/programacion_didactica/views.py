from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from programacion_didactica.models import Unidad, InstEvaluacion, PondRA, PondCriterio, PondCritUD
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import request
from core.mixins import coreMixin , deleteMixin
from core.models import Modulo
from programacion_didactica.forms import UnidadForm, InstEvaluacionForm, PondRAForm, PondCriterioForm, PondCritUDForm
from django.contrib.messages.views import SuccessMessageMixin

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# UD6.7.a

class UnidadListView(ListView):
    model = Unidad
    template_name = 'programacion_didactica/unidad_list.html'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



    def get_queryset(self):
        orden = self.request.GET.get('orden', None)
        queryset = Unidad.objects.all()
        if orden:
            if orden == 'asc':
                queryset = queryset.order_by('id')
            elif orden == 'desc':
                queryset = queryset.order_by('-id')

        return queryset



class UnidadDetailView(DetailView):
    model = Unidad
    template_name = 'programacion_didactica/unidad_detail.html'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class InstEvListView(ListView):
    model = InstEvaluacion
    template_name = 'programacion_didactica/ie_list.html'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #UD7.2.j
    def get_queryset(self):
        orden = self.request.GET.get('orden', None)
        queryset = InstEvaluacion.objects.all()
        if orden:
            if orden == 'asc':
                queryset = queryset.order_by('id')
            elif orden == 'desc':
                queryset = queryset.order_by('-id')

        return queryset

class InstEvDetailView(DetailView):
    model = InstEvaluacion
    template_name = 'programacion_didactica/ie_detail.html'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class PondRAListView(ListView):
    model = PondRA
    template_name = 'programacion_didactica/pond_ra_list.html'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #UD7.2.j
    def get_queryset(self):
        orden = self.request.GET.get('orden', None)
        queryset = PondRA.objects.all()
        if orden:
            if orden == 'asc':
                queryset = queryset.order_by('id')
            elif orden == 'desc':
                queryset = queryset.order_by('-id')

        return queryset

class PondRADetailView(DetailView):
    model = PondRA
    template_name = 'programacion_didactica/pond_ra_detail.html'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class PondCritListView(ListView):
    model = PondCriterio
    template_name = 'programacion_didactica/pond_ce_list.html' 
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #UD7.2.j
    def get_queryset(self):
        orden = self.request.GET.get('orden', None)
        queryset = PondCriterio.objects.all()
        if orden:
            if orden == 'asc':
                queryset = queryset.order_by('id')
            elif orden == 'desc':
                queryset = queryset.order_by('-id')

        return queryset

class PondCritDetailView(DetailView):
    model = PondCriterio
    template_name = 'programacion_didactica/pond_ce_detail.html'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class PondCritUDListView(ListView):
    model = PondCritUD
    template_name = 'programacion_didactica/pond_ce_ud_list.html'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #UD7.2.j
    def get_queryset(self):
        orden = self.request.GET.get('orden', None)
        queryset = PondCritUD.objects.all()
        if orden:
            if orden == 'asc':
                queryset = queryset.order_by('id')
            elif orden == 'desc':
                queryset = queryset.order_by('-id')

        return queryset



class PondCritUDDetailView(DetailView):
    model = PondCritUD
    template_name = 'programacion_didactica/pond_ce_ud_detail.html'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#UD7.2.a

class UDCreateView(coreMixin, SuccessMessageMixin, CreateView):
    model= Unidad
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('ud_create')
    #UD7.2.c
    titulo_actualizacion = ''
    titulo_creacion = 'crear una unidad'
    url_borrado = 'unidad_delete'    
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    form_class = UnidadForm

    def get_success_message(self, cleaned_data):
        return "UD '{}' creado exitosamente".format(str(self.object))
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('unidad_update', kwargs={'pk': object.id})

#UD7.2.a
class UDUpdateView(coreMixin, SuccessMessageMixin, UpdateView):
    model = Unidad
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('ud_update')
    #UD7.2.c
    titulo_actualizacion = 'actualizar una unidad'
    titulo_creacion = ''
    url_borrado = 'unidad_delete'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    form_class = UnidadForm

    def get_success_message(self, cleaned_data):
        return "UD '{}' actualizado exitosamente".format(str(self.object))
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('unidad_update', kwargs={'pk': object.id})

#UD7.2.a
class UDDeleteView(deleteMixin, DeleteView):
    model = Unidad
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('ud_list')
    #UD7.2.f
    titulo = 'Unidad'
    mensaje_confirmacion = '¿Estas seguro de que quieres borrar la unidad?'
    #UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#UD7.2.a
class InstEvaluacionCreateView(coreMixin, SuccessMessageMixin, CreateView):
    model= InstEvaluacion
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('ie_create')
    #UD7.2.c
    titulo_actualizacion = ''
    titulo_creacion = 'crear un instrumento de evaluacion'
    url_borrado = 'ie_delete'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    form_class = InstEvaluacionForm

    def get_success_message(self, cleaned_data):
        return "IE '{}' creado exitosamente".format(str(self.object))
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('ie_update', kwargs={'pk': object.id})

#UD7.2.a
class InstEvaluacionUpdateView(coreMixin, SuccessMessageMixin, UpdateView):
    model = InstEvaluacion
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('ie_update')
    #UD7.2.c
    titulo_actualizacion = 'actualizar un instrumento evaluacion'
    titulo_creacion = ''
    url_borrado = 'ie_delete'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    form_class = InstEvaluacionForm

    def get_success_message(self, cleaned_data):
        return "IE '{}' actualizado exitosamente".format(str(self.object))
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('ie_update', kwargs={'pk': object.id})

#UD7.2.a
class InstEvaluacionDeleteView(deleteMixin, DeleteView):
    model = InstEvaluacion
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('ie_list')
    #UD7.2.f
    titulo = 'Instrumento de evaluación'
    mensaje_confirmacion = '¿Estas seguro de que quieres borrar el instrumento de evaluacion?'
 #UD8.3   
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#UD7.2.a
class PonderacionRACreateView(coreMixin, SuccessMessageMixin, CreateView):
    model= PondRA
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('pond_ra_create')
    #UD7.2.c
    titulo_actualizacion = ''
    titulo_creacion = 'crear un resultado de aprendizaje'
    url_borrado = 'pond_ra_delete'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    form_class = PondRAForm

    def get_success_message(self, cleaned_data):
        return "Pond RA '{}' creado exitosamente".format(str(self.object))
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('pond_ra_update', kwargs={'pk': object.id})

#UD7.2.a
class PonderacionRAUpdateView(coreMixin, SuccessMessageMixin, UpdateView):
    model = PondRA
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('pond_ra_update')
    #UD7.2.c
    titulo_actualizacion = 'ctualizar un resultado de aprendizaje'
    titulo_creacion = ''
    url_borrado = 'pond_ra_delete'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    form_class = PondRAForm

    def get_success_message(self, cleaned_data):
        return "Pond RA '{}' actualizado exitosamente".format(str(self.object))
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('pond_ra_update', kwargs={'pk': object.id})

#UD7.2.a
class PonderacionRADeleteView(deleteMixin, DeleteView):
    model = PondRA
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('pond_ra_list')
    #UD7.2.f
    titulo = 'Ponderación de resultado de aprendizaje'
    mensaje_confirmacion = '¿Estas seguro de que quieres borrar la ponderacion del resultado de aprendizaje?'
#UD8.3  
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
#UD7.2.a
class PondCriterioCreateView(coreMixin, SuccessMessageMixin, CreateView):
    model= PondCriterio
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('pond_ce_create')
    #UD7.2.c
    titulo_actualizacion = ''
    titulo_creacion = 'crear una ponderacion de un criterio de evaluacion'
    url_borrado = 'pond_ce_delete'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    form_class = PondCriterioForm

    def get_success_message(self, cleaned_data):
        return "Pond CE '{}' creado exitosamente".format(str(self.object))
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('pond_ce_update', kwargs={'pk': object.id})

#UD7.2.a
class PondCriterioUpdateView(coreMixin, SuccessMessageMixin, UpdateView):
    model = PondCriterio
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('pond_ce_update')
    #UD7.2.c
    titulo_actualizacion = 'actualizar una ponderacion de un criterio de evaluacion'
    titulo_creacion = ''
    url_borrado = 'pond_ce_delete'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    form_class = PondCriterioForm

    def get_success_message(self, cleaned_data):
        return "Pond CE '{}' actualizado exitosamente".format(str(self.object))
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('pond_ce_update', kwargs={'pk': object.id})

#UD7.2.a
class PondCriterioDeleteView(deleteMixin, DeleteView):
    model = PondCriterio
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('pond_ce_list')
    #UD7.2.f
    titulo = 'Ponderación de critério de evaluación'
    mensaje_confirmacion = '¿Estas seguro de que quieres borrar la ponderacion del criterio de evaluacion?'
#UD8.3   
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
        
#UD7.2.a
class PondCriterioUDCreateView(coreMixin, SuccessMessageMixin, CreateView):
    model= PondCritUD
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('pond_ce_ud_create')
    #UD7.2.c
    titulo_actualizacion = ''
    titulo_creacion = 'crear una ponderacion de un criterio de evaluacion por unidad'
    url_borrado = 'pond_ce_ud_delete'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    form_class = PondCritUDForm

    def get_success_message(self, cleaned_data):
        return "Pond CE por UD '{}' creado exitosamente".format(str(self.object))
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('pond_ce_ud_update', kwargs={'pk': object.id})


#UD7.2.a
class PondCriterioUDUpdateView(coreMixin, SuccessMessageMixin, UpdateView):
    model = PondCritUD
    template_name = 'common/base_create_update.html'
    #success_url = reverse_lazy('pond_ce_ud_update')
    #UD7.2.c
    titulo_actualizacion = 'actualizar una ponderacion de un criterio de evaluacion por unidad'
    titulo_creacion = ''
    url_borrado = 'pond_ce_ud_delete'
#UD8.3
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    form_class = PondCritUDForm

    def get_success_message(self, cleaned_data):
        return "Pond CE por UD '{}' actualizado exitosamente".format(str(self.object))
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('pond_ce_ud_update', kwargs={'pk': object.id})


#UD7.2.a
class PondCriterioUDDeleteView(deleteMixin, DeleteView):
    model = PondCritUD
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('pond_ce_ud_list')
    #UD7.2.f
    titulo = 'Ponderación de critério de evaluación por unidad'
    mensaje_confirmacion = '¿Estas seguro de que quieres borrar la ponderacion del criterio de evaluacion por unidad?'
#UD8.3    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
