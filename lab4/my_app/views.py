from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


# from my_app.models import Product


def base(request):
    return render(request, 'home_page.html')


class CoffeesView(View):

    def get(self, request):
        data = {
            'coffees': [
                {'title': 'Cappuccino', 'subtitle': 'Капучино', 'img': '/static/media/cappucino.jpg', 'id': 3},
                {'title': 'Latte', 'subtitle': 'Латте', 'img': '/static/media/latte.jpg', 'id': 4},
                {'title': 'Macchiato', 'subtitle': 'Макиато', 'img': '/static/media/machiato.jpg', 'id': 5},
                {'title': 'Mocha', 'subtitle': 'Моккачино', 'img': '/static/media/mocha.jpg', 'id': 6},
            ]
        }
        return render(request, 'coffees.html', data)


class CoffeeView(View):


    def get(self, request, id):
        data = {
            'coffee': {
                'title': "",
                'id': id
            }
        }
        return render(request, 'coffee.html', context=data)


class SyrupsView(View):

    def get(self, request):
        data = {
            'syrups': [
                {'title': 'Caramel', 'id': 1},
                {'title': 'Vanila', 'id': 2},
                {'title': 'Halzenut', 'id': 3},
                {'title': 'French Vanilla', 'id': 4},
                {'title': 'Cocount', 'id': 5},
            ]
        }
        return render(request, 'syrups.html', data)


class SyrupView(View):

    def get(self, request, id):
        data = {
            'syrop': {
                'title': '',
                'id': id
            }
        }
        return render(request, 'syrup.html', context=data)
