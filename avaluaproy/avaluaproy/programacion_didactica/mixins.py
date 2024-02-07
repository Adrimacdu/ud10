#UD10.3.b
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class deleteMixin_api():
    def delete(self, request, *args, **kwargs):
        try:
                super().delete(request, *args, **kwargs)
        except:
            messages.error(request, "No se puede realizar la operación de borrado porque existen dependencias.")
            return HttpResponseRedirect(reverse('api'))