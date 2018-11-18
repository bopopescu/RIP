from django.shortcuts import render

# Create your views here.
from django.views import View

from anime.models import AnimeModel


class AnimeView(View):
    def get(self, request):
        #anime = AnimeModel(name="Ведьмочка Рурумо", description="Лехино аниме", author="Ватару Ватанабэ")
        #anime.save()
        animes = AnimeModel.objects.all()
        data = {
            'animes': animes
        }
        return render(request, 'animeinfo.html', data)
