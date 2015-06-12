# -*- coding: UTF-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import *
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView, CreateView, View
from .models import *
from django.core.mail import EmailMultiAlternatives
import random, string
from django.contrib.auth.models import User



class index(TemplateView):
    template_name = 'base.html'

class ErrorActiveView(TemplateView):
    template_name = 'inicio/error_activacion.html'
    
class UserActiveErrorView(TemplateView):
    template_name = 'inicio/usuario_ya_activo.html'

class UserActiveView(TemplateView):
    template_name = 'inicio/usuario_activo.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'inicio/register.html'
    
    def form_valid(self, form):
        form.instance.is_active = False
        form.instance.act = ''.join(random.choice(string.ascii_uppercase + string.digits)
                                               for n in range(20))
        usuario = form.cleaned_data.get('email')
        html_content = 'Por favor visite http://127.0.0.1:8000/activar/%s/ para activar su cuenta' \
                       %(form.instance.act)
        msg = EmailMultiAlternatives('Código de Activación',html_content,\
                                     'friends_77_3@hotmail.com',[usuario])
        msg.attach_alternative(html_content,'text/html') # Definimos el contenido como HTML
        msg.send() # Enviamos el correo
        return super(UserCreateView, self).form_valid(form)


class ActivteUserView(View):
    
    def dispatch(self, *args, **kwargs):
        self.codigo = self.kwargs['codigo']
        return super(ActivteUserView, self).dispatch(*args, **kwargs)
        
    def get(self, request, *args, **kwargs):
        try:
            self.usuario = User.objects.get(act=self.codigo)
            if self.usuario.is_active == False:
                self.usuario.is_active = True
                self.usuario.save()
                return HttpResponseRedirect("/activo_exito/")
            else:
                return HttpResponseRedirect("/activo/")
        except UserRegister.DoesNotExist:
            return HttpResponseRedirect('/error_activacion')