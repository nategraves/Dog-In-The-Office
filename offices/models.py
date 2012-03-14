from django.db import models

from plusplus.models import ModelBase

class Office(ModelBase):

    name = models.CharField(max_length=255)
    url = models.URLField()
    photo = models.ImageField(upload_to='offices/')

    def __unicode__ (self):
        return self.name