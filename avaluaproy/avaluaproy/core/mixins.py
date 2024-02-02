from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class coreMixin():
        #UD7.2.d
        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['titulo_actualizacion'] = self.titulo_actualizacion
                context['titulo_creacion'] = self.titulo_creacion
                context['url_borrado'] = self.url_borrado
                return context
                

class deleteMixin():
        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['titulo'] = self.titulo
                context['mensaje_confirmacion'] = self.mensaje_confirmacion
                return context

        def form_valid(self, request, *args, **kwargs):
                try:
                        super().delete(*args, request, **kwargs)
                except:
                        messages.error(self.request, "Existen dependencias para el objeto {}. Elimine antes dichas dependencias".format(self.object))
                return HttpResponseRedirect(reverse('home'))