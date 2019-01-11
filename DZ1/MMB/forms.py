from datetime import date

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from MMB.models import BandModel, MemberModel, MembershipModel #, UserModel


class LoginForm(forms.Form):
    """ Base class for authenticating users. Extend this to get a form that accepts
    username/password logins. """
    username = UsernameField(
        label='Логин',
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5, label='Логин')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите пароль')
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    avatar = forms.ImageField(label='Аватар')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                     'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                                                     'placeholder': 'Введите Логин'})

        self.fields['password'].widget.attrs.update({'type': 'password', 'class': 'form-control',
                                                     'id': 'exampleInputPassword1', 'placeholder': 'Пароль'})

        self.fields['password2'].widget.attrs.update({'type': 'password', 'class': 'form-control',
                                                      'id': 'exampleInputPassword1', 'placeholder': 'Повторите пароль'})

        self.fields['email'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                  'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                                                  'placeholder': 'Введите Email'})

        self.fields['first_name'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                       'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                                                       'placeholder': 'Введите Имя'})

        self.fields['last_name'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                      'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                                                      'placeholder': 'Введите Фамилию'})
        self.fields['avatar'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                      'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                                                      'placeholder': 'Выберите аватар'})


class EnterForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    def __init__(self, *args, **kwargs):
        super(EnterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                     'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                                                     'placeholder': 'Введите Логин'})

        self.fields['password'].widget.attrs.update({'type': 'password', 'class': 'form-control',
                                                     'id': 'exampleInputPassword1', 'placeholder': 'Пароль'})


class AddBandForm(forms.Form):
    class Meta:
        model = BandModel
        exclude = ['members']

    name = forms.CharField(label="Название")
    # members = forms.ModelMultipleChoiceField(label="Выберите членов группы", queryset=MemberModel.objects.all())  # чтобы только фамилии
    genre = forms.CharField(label="Жанр")
    history = forms.CharField(label="О группе")
    pic = forms.FileField(label="Герб группы", allow_empty_file=True)

    def __init__(self, *args, **kwargs):  # полписи в полях заполнения
        super(AddBandForm, self).__init__(*args, **kwargs)
        self.fields['pic'].widget.attrs.update({'name': 'pic', 'label': 'Загрузить', 'type': 'file',
                                                'class': 'form-control-file', 'id': 'pic'})


class AddMemberForm(forms.Form):
    class Meta:
        model = MemberModel

    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")
    birthdate = forms.DateField(label="Дата рождения")
    deathdate = forms.DateField(label="Дата смерти", required=False)
    country = forms.CharField(label="Страна")
    photo = forms.FileField(label="Фото исполнителя", allow_empty_file=True)

    def __init__(self, *args, **kwargs):
        super(AddMemberForm, self).__init__(*args, **kwargs)
        self.fields['birthdate'].widget.attrs.update({'class': 'form-control', 'placeholder': 'mm/dd/yyyy'})
        self.fields['deathdate'].widget.attrs.update({'class': 'form-control', 'placeholder': 'mm/dd/yyyy'})
        self.fields['photo'].widget.attrs.update({'name': 'photo', 'label': 'Загрузить', 'type': 'file',
                                                  'class': 'form-control-file', 'id': 'photo'})


class MembershipForm(forms.Form):
    class Meta:
        model = MembershipModel
        exclude = ['id_member_FK', 'id_band_FK']

    id_member_FK = forms.ModelChoiceField(queryset=MemberModel.objects.all())
    id_band_FK = forms.ModelChoiceField(queryset=BandModel.objects.all(), required=False)
    function = forms.CharField(label="Должность")
    statuss = forms.BooleanField(label="Все еще в группе?", required=False)


class UpdateProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


'''class UpdateAvaForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ('avatar',)'''
