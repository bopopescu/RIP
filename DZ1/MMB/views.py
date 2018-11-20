from django.shortcuts import render
from django.views import View
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