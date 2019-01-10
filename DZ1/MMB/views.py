import json
import math

from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, UpdateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from MMB.forms import RegistrationForm, EnterForm, LoginForm, AddBandForm, AddMemberForm, MembershipForm, \
    UpdateProfileForm
from MMB.models import MemberModel, BandModel, MembershipModel, UserModel


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


class ProfileView(View):
    def get(self, request):
        user = User.objects.get(id=auth.get_user(request).id)
        avatar = UserModel.objects.get(username=user.username)
        form = UpdateProfileForm(
            initial=model_to_dict(user, fields=['username', 'password', 'email', 'first_name', 'last_name']))
        return render(request, 'profile.html',
                      {'user': user, 'form':form, 'username': auth.get_user(request).username, 'avatar': avatar})

    def post(self, request):
        #form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        #if form.is_valid():
         #   form.save()
        if request.method == 'POST':
            if 'logout' in request.POST:
                auth.logout(request)
                return HttpResponseRedirect('/login/')
            if 'update' in request.POST:
                return HttpResponseRedirect('/update_profile/')


class UpdateProfileView(View):
    def get(self, request):
        user = User.objects.get(id=auth.get_user(request).id)
        avatar = UserModel.objects.get(username=user.username)
        form = UpdateProfileForm(
            initial=model_to_dict(user, fields=['username', 'password', 'email', 'first_name', 'last_name']))
        return render(request, 'update_profile.html',
                      {'form': form, 'user': user, 'username': auth.get_user(request).username, 'avatar': avatar})

    def post(self, request):
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        if request.method == 'POST':
            if 'logout' in request.POST:
                auth.logout(request)
                return HttpResponseRedirect('/login/')
            if 'updated' or 'update' in request.POST:
                return HttpResponseRedirect('/profile/')


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
        '''elements_on_page = 2
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
    index += 1  # index=3

if len(row) > 0:  # 2 группы
    rows.append(row)'''

        paginator = Paginator(BandModel.objects.all(), 2)
        page = request.GET.get('page')
        try:
            rows = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            rows = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            rows = paginator.page(paginator.num_pages)

        members = MemberModel.objects.all()
        form = AddBandForm(request.POST or None)

        return render(request, 'bands_main.html',
                      {'members': members, 'bands': rows, 'page': page,
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
                    id_band_FK = BandModel.objects.get(id=id)
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
                avatar = UserModel(
                    username=form.cleaned_data['username'],
                    ava='/static/media/ava/default.jpg')
                user.save()
                avatar.save()
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
        return render(request, 'endReg.html', {'username': auth.get_user(request).username})

    def post(self, request):
        if request.method == 'POST':
            if 'logout' in request.POST:
                auth.logout(request)
                return HttpResponseRedirect('/login/')
            if 'band' in request.POST:
                return HttpResponseRedirect('/band/page=1')
            if 'member' in request.POST:
                return HttpResponseRedirect('/member/')
            if 'sign_in' in request.POST:
                return HttpResponseRedirect('/login/')
            elif 'sign_up' in request.POST:
                return HttpResponseRedirect('/registration/')
