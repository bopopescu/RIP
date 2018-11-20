from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from MMB.forms import RegistrationForm, EnterForm
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
            'members': members
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
            'bands': bands
        }
        return render(request, 'bands.html', data)


class BandView(View):
    def get(self, request, id):
        band = BandModel.objects.get(id=int(id))
        return render(request, 'band.html', {'band': band})


class LogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return HttpResponseRedirect(reverse('login'))


def registration(request):
    # Регаемся
    errors = []
    success = ''
    if request.method == 'POST':
        if 'signIn' in request.POST:
            return HttpResponseRedirect('/login/')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

            users = User.objects.all()
            usernames = []
            for x in users:
                usernames.append(x.username)

            if form.cleaned_data['password'] != form.cleaned_data['password2']:
                errors.append('Пароли должны совпадать')
            elif usernames.count(username) != 0:
                errors.append('Такой логин уже занят')
            else:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name']
                )
                user.save()
                return HttpResponseRedirect('/login/')

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form, 'errors': errors, 'success': success})


def login(request):
    errors = []
    if request.method == 'POST':
        if 'reg' in request.POST:
            return HttpResponseRedirect('/registration/')
        form = EnterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/login/')
            else:
                errors.append('Неверно введён логин или пароль')
    else:
        form = EnterForm()
    return render(request, 'login.html', {'form': form, 'errors': errors})
