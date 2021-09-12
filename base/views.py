from re import template
from django.forms.models import ModelForm
from django.views.generic.base import TemplateResponseMixin
from base.models import PasswordModeling
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import PasswordModeling
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.



class RegisterView(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    
    success_url = reverse_lazy('list-passwords')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('list-passwords')
        return super(RegisterView, self).get(*args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

class LoginForPassword(LoginView):
    template_name = 'base/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list-passwords')


class PasswordList(LoginRequiredMixin, ListView):
    model = PasswordModeling
    context_object_name = 'passwords'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['passwords'] = context['passwords'].filter(user=self.request.user)
        return context

class PasswordDetail(LoginRequiredMixin, DetailView):
    model = PasswordModeling
    context_object_name = 'password_in_detail'

class PasswordCreate(LoginRequiredMixin, CreateView):
    model = PasswordModeling
    fields = ["site", "url_of_site", "email", "passwords"]
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PasswordCreate, self).form_valid(form)


    def get_success_url(self):
        return reverse('detail-password',args=(self.object.id,))






class PasswordUpdate(LoginRequiredMixin, UpdateView):
    model = PasswordModeling
    fields = ["site", "url_of_site", "email", "passwords"]


    

    def get_success_url(self):
        return reverse('detail-password',args=(self.object.id,))


class PasswordDelete(LoginRequiredMixin, DeleteView):
    model = PasswordModeling
    context_object_name = 'password'
    success_url = reverse_lazy('list-passwords')