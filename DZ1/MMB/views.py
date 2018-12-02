import json
import math

from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from MMB.forms import RegistrationForm, EnterForm, LoginForm, AddBandForm, AddMemberForm, MembershipForm
from MMB.models import MemberModel, BandModel, MembershipModel


class Start(View):
    def get(self, request):
        return render(request, 'main_page.html')

    def post(self, request):
        if request.method == 'POST':
            if 'sign_in' in request.POST:
                return HttpResponseRedirect('/login/')
            elif 'sign_up' in request.POST:
                return HttpResponseRedirect('/registration/')
            elif 'logout' in request.POST:
                auth.logout(request)
                return HttpResponseRedirect('/login/')


class MembersView(View):
    def get(self, request):
        members = MemberModel.objects.all()

        form = AddMemberForm(request.POST or None)
        return render(request, 'members.html',
                      {'members': members, 'form': form, 'username': auth.get_user(request).username})

    def post(self, request):
        if request.method == 'POST':
            if 'sign_in' in request.POST:
                return HttpResponseRedirect('/login/')
            elif 'sign_up' in request.POST:
                return HttpResponseRedirect('/registration/')
            elif 'logout' in request.POST:
                auth.logout(request)
                return HttpResponseRedirect('/login/')
            elif 'add_member' in request.POST:
                form = AddMemberForm(request.POST, request.FILES)
                if form.is_valid():
                    member = MemberModel(
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'],
                        birthdate=form.cleaned_data['birthdate'],
                        deathdate=form.cleaned_data['deathdate'],
                        country=form.cleaned_data['country'],
                        photo=form.cleaned_data['photo'])
                    member.save()
                    url = '/member/' + str(member.id)
                    return HttpResponseRedirect(url)  # заменить на сообщение об ошибке


class MemberView(View):
    def get(self, request, id):
        member = MemberModel.objects.get(id=int(id))
        return render(request, 'member.html', {'member': member, 'username': auth.get_user(request).username, 'id': id})

    def post(self, request, id):
        if request.method == 'POST':
            if 'sign_in' in request.POST:  # по жмяку на кнопку
                return HttpResponseRedirect('/login/')
            elif 'sign_up' in request.POST:
                return HttpResponseRedirect('/registration/')
            elif 'logout' in request.POST:
                auth.logout(request)
                return HttpResponseRedirect('/login/')


class BandsView(ListView):
    def get(self, request, page=1):
        # member = MemberModel(first_name="Брайан", last_name="Мэй", birthdate='1947-07-19', country='Великобритания', photo='May.jpg')
        # member.save()
        elements_on_page = 5
        elements_in_row = 1
        bands = BandModel.objects.all()
        pages_count = math.ceil(len(bands) / elements_on_page)

        start_index = (int(page) - 1) * elements_on_page
        end_index = start_index + elements_on_page
        bands = bands[start_index:end_index]

        index = 1
        rows = []
        row = []
        for band in bands:
            row.append(band)
            index += 1

        if len(row) > 0:
            rows.append(row)

        members = MemberModel.objects.all()
        form = AddBandForm(request.POST or None)

        return render(request, 'bands_main.html',
                      {'members': members, 'bands': rows, 'page': page, 'pages_count': pages_count,
                       'username': auth.get_user(request).username, 'form': form})

    def post(self, request):
        if request.method == 'POST':
            if 'sign_in' in request.POST:
                return HttpResponseRedirect('/login/')
            elif 'sign_up' in request.POST:
                return HttpResponseRedirect('/registration/')
            elif 'logout' in request.POST:
                auth.logout(request)
                return HttpResponseRedirect('/login/')
            elif 'add_band' in request.POST:
                if auth.get_user(request):
                    errors = []
                    form = AddBandForm(request.POST, request.FILES)
                    if form.is_valid():
                        band = BandModel(
                            name=form.cleaned_data['name'],
                            members=form.cleaned_data['members'],
                            genre=form.cleaned_data['genre'],
                            history=form.cleaned_data['history'],
                            pic=form.cleaned_data['pic'])
                        band.save()
                        MembershipModel.save_m2m()
                        MemberModel.save_m2m()
                        url = '/band/' + str(band.id)
                        return HttpResponseRedirect(url)
                    # json_response = json.dumps({'errors': errors, 'msg': msg})
                    # return HttpResponse(content_type="application/json")
                else:
                    return HttpResponseRedirect('/login/')  # заменить на сообщение об ошибке


class BandView(View):
    def get(self, request, id):
        band = BandModel.objects.get(id=int(id))
        members = band.members.all()
        new_members = MemberModel.objects.all()

        form = MembershipForm(request.POST or None)
        return render(request, 'band.html',
                      {'band': band, 'members': members, 'new_members': new_members, 'form': form,
                       'username': auth.get_user(request).username, 'id': id})

    def post(self, request, id):
        if request.method == 'POST':
            errors = []
            if 'sign_in' in request.POST:
                return HttpResponseRedirect('/login/')
            elif 'sign_up' in request.POST:
                return HttpResponseRedirect('/registration/')
            elif 'logout' in request.POST:
                auth.logout(request)
                return HttpResponseRedirect('/login/')
            elif 'add_members' in request.POST:
                form = MembershipForm(request.POST, request.FILES)

                if form.is_valid():
                    id_band_FK=BandModel.objects.get(id=id)
                    membership = MembershipModel(
                        id_member_FK=form.cleaned_data['id_member_FK'],
                        id_band_FK=id_band_FK,
                        function=form.cleaned_data['function'],
                        statuss=form.cleaned_data['statuss'])
                    membership.save()
                    # BandModel.save()
                    url = '/band/' + str(id)
                    return HttpResponseRedirect(url)
                # заменить на сообщение об ошибке


def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/login/')


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
    names_dict = {}
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if 'reg' in request.POST:
            return HttpResponseRedirect('/registration/')
        form = EnterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            names_dict = {x: request.POST.get(x, "") for x in ["username", "password"]}
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/start/')
            else:
                errors.append('Неверно введён логин или пароль')
    else:
        form = EnterForm()
    return render(request, 'login.html', {'form': form, 'errors': errors, 'names_dict': names_dict})


class TitlesView(View):
    def get(self, request):
        amount_bands = BandModel.objects.all().count()
        amount_pages = 0
        if amount_bands % 3 == 1 or amount_bands % 3 == 2:
            amount_pages = int(amount_bands / 3 + 1)
        elif amount_bands % 3 == 0:
            amount_pages = amount_bands / 3
        return render(request, 'endReg.html', {'pages': amount_pages, 'username': auth.get_user(request).username})

    def post(self, request):
        if request.method == 'POST':
            if 'logout' in request.POST:
                auth.logout(request)
                return HttpResponseRedirect('/login/')
            if 'band' in request.POST:
                return HttpResponseRedirect('/band/')
            if 'member' in request.POST:
                return HttpResponseRedirect('/member/')
            if 'sign_in' in request.POST:
                return HttpResponseRedirect('/login/')
            elif 'sign_up' in request.POST:
                return HttpResponseRedirect('/registration/')
