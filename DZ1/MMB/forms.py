from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm

from MMB.models import BandModel, MemberModel, MembershipModel


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


class AddBandForm(forms.ModelForm):
    class Meta:
        model = BandModel
        # fields = ['name', 'genre', 'history', 'pic']
        exclude = ['/static/media/']


    name = forms.CharField(label="Название")
    members = forms.ModelMultipleChoiceField(label="Выберите членов группы", queryset=MemberModel.objects.all())  # чтобы только фамилии
    genre = forms.CharField(label="Жанр")
    history = forms.CharField(label="О группе")
    pic = forms.FileField(label="Выберите файл", allow_empty_file=True)

    def __init__(self, *args, **kwargs):  # полписи в полях заполнения
        super(AddBandForm, self).__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название'})
        # self.fields['genre'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите жанр'})
        self.fields['members'].widget = forms.widgets.MultipleHiddenInput()
        self.fields["members"].queryset = MemberModel.objects.all()


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = MemberModel
        exclude = ['/static/media/']

    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")
    birthdate = forms.DateField(label="Дата рождения", input_formats='%d/%m/%Y')
    deathdate = forms.DateField(label="Дата смерти", input_formats='%d/%m/%Y')
    country = forms.CharField(label="Страна")
    photo = forms.FileField(label="Выберите файл", allow_empty_file=True)

    def __init__(self, *args, **kwargs):
        super(AddMemberForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['birthdate'].widget.attrs.update({'class': 'form-control', 'placeholder': 'dd/mm/yyyy'})
        self.fields['deathdate'].widget.attrs.update({'class': 'form-control', 'placeholder': 'dd/mm/yyyy'})
