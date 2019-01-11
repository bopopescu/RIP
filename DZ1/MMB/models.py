from django.db import models

from django.contrib.auth.models import User


class MemberModel(models.Model):
    class Meta:
        db_table = 'member'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    deathdate = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=30)
    photo = models.FileField(default='static/media/default.jpg', upload_to='static/media/', blank=True)


def __str__(self):
    return self.last_name


class BandModel(models.Model):
    class Meta:
        db_table = 'band'

    name = models.CharField(max_length=30)
    members = models.ManyToManyField(MemberModel, through='MembershipModel', null=True, blank=True)
    genre = models.CharField(max_length=50)
    history = models.CharField(max_length=255, null=True, blank=True)
    pic = models.FileField(default='static/media/default.jpg', upload_to='static/media/')


def __str__(self):
    return self.name


class MembershipModel(models.Model):
    class Meta:
        db_table = 'membership'

    id_member_FK = models.ForeignKey(MemberModel, on_delete=models.CASCADE, db_column='id_member_FK',
                                     related_name='id_member_FK')
    id_band_FK = models.ForeignKey(BandModel, on_delete=models.CASCADE, db_column='id_band_FK',
                                   related_name='id_band_FK')
    function = models.CharField(max_length=50)
    statuss = models.BooleanField(default=1)


def __str__(self):
    return "Band: {}, Member: {}".format(self.id_band_FK, self.id_member_FK)


'''class UserModel(models.Model):
    class Meta:
        db_table = 'avatar'

#    nameofuser = models.OneToOneField(User, models.CASCADE, primary_key=True, db_column='nameofuser',
#                                      related_name='nameofuser')
#    ava = models.FileField(default='static/media/ava/default.jpg', upload_to='static/media/ava/')
    nameofuser = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='static/media/default.jpg', upload_to='static/media/ava/')

def __str__(self):
    return "User: {}, Avatar: {}".format(self.nameofuser, self.ava)'''
