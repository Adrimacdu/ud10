from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import RedirectView
from django.contrib.auth import logout
#UD8.2.b
class LoginFormView(LoginView):
    template_name = 'login/login.html'
#UD8.3
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/panel')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesion'
        return context
#UD8.2.c
class LogoutRedirectView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
