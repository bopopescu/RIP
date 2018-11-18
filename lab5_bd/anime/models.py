from django.db import models


class AnimeModel(models.Model):
    class Meta:
        db_table='anime_Table'
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=50)

    def __unicode__(self):
        dict = {}
        dict['name'] = self.name
        dict['description'] = self.description
        dict['author'] = self.author
        return dict
