from django.contrib import auth
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import FormView

from MMB.forms import RegistrationForm, LoginForm
from MMB.models import MemberModel, BandModel


class Start(View):
    def get(self, request):
        return render(request, 'main_page.html')

class MembersView(View):
    def get(self, request):
        # member = MemberModel(first_name="Брайан", last_name="Мэй", birthdate='1947-07-19', country='Великобритания', photo='May.jpg')
        # member.save()
        members = MemberModel.objects.all()
        data = {
            'members':members
        }
        return render(request, 'members.html', data)

class MemberView(View):
    def get(self, request, id):
        member = MemberModel.objects.get(id=int(id))
        return render(request, 'member.html', {'member': member})


class BandsView(View):
    def get(self, request):
        # member = MemberModel(first_name="Брайан", last_name="Мэй", birthdate='1947-07-19', country='Великобритания', photo='May.jpg')
        # member.save()
        bands = BandModel.objects.all()
        data = {
            'bands':bands
        }
        return render(request, 'bands.html', data)

class BandView(View):
    def get(self, request, id):
        band = BandModel.objects.get(id=int(id))
        return render(request, 'band.html', {'band': band})



class LoginView(LoginView):
    template_name = 'login.html'  # в ContextData есть form, так что не прописываем
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form_action'] = reverse('login')  # в urls
        return data

    def get_success_url(self):
        return reverse('chat_get')
# при использовании reverse url's не привязаны к путям->
# можем менять как угодно

class LogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return HttpResponseRedirect(reverse('login'))


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = "registration.html"

    def get_success_url(self):
        return reverse('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)