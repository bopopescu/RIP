from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BandModel)
admin.site.register(MembershipModel)
admin.site.register(MemberModel)
admin.site.register(UserModel)