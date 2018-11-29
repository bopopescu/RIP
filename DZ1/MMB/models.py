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
    return '%s %s' % (self.first_name, self.last_name)


class BandModel(models.Model):
    class Meta:
        db_table = 'band'

    name = models.CharField(max_length=30)
    members = models.ManyToManyField(MemberModel, through='MembershipModel', null=True, blank=True)
    genre = models.CharField(max_length=50)
    history = models.CharField(max_length=255, null=True, blank=True)
    pic = models.FileField(default='static/media/default.jpg', upload_to='static/media/')


def __str__(self):
    return "Name: {}".format(self.name)


class MembershipModel(models.Model):
    class Meta:
        db_table = 'membership'

    id_member_FK = models.ForeignKey(MemberModel, on_delete=models.CASCADE, db_column='id_member_FK')
    id_band_FK = models.ForeignKey(BandModel, on_delete=models.CASCADE, db_column='id_band_FK')
    function = models.CharField(max_length=50)
    statuss = models.BooleanField(default=1)


def __str__(self):
    return "Band: {}, Member: {}".format(self.id_band_FK, self.id_member_FK)
