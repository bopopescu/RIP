from django.db import models

# Create your models here.
class Anime(models.Model):
    id=models.IntegerField(11, primary_key=True)
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=255)
    author=models.CharField(max_length=50)

    def __unicode__(self):
        dict={}
        dict['id']=self.id
        dict['name']=self.name
        dict['description']=self.description
        dict['author']=self.author
        return dict


class User(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    sex=models.CharField(max_length=1)
    birthdate=models.DateTimeField()


    def __unicode__(self):
        dict = {}
        dict['id'] = self.id
        dict['first_name'] = self.first_name
        dict['last_name'] = self.last_name
        dict['sex'] = self.sex
        dict['birthdate']=self.birthdate
        return dict


class Review(models.Model):
    review_id=models.IntegerField(11, primary_key=True)
    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

    def __unicode__(self):
        dict = {}
        dict['review_id'] = self.review_id
        dict['anime_id'] = self.anime_id
        dict['user_id'] = self.user_id
        dict['content'] = self.content
        return dict