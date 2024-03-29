from django.db import models
from django.contrib.auth.models import User

from plusplus.models import ModelBase
from offices.models import Office

DOG_SIZES = (
    ("S", "Small - 0-15 lbs"),
    ("M", "Medium - 16-30 lbs"),
    ("L", "Large - 31-50 lbs"),
    ("X", "Extra Large - 51+ lbs"),
)

class Dog(ModelBase):

    name = models.CharField(max_length=255)
    size = models.CharField(max_length=1, choices=DOG_SIZES)
    photo = models.ImageField(upload_to='dogs/')
    office = models.ForeignKey(Office)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return '%s at %s' % (self.name, self.office.name)

    class Meta:
        db_table = 'dog'

class DogDay(models.Model):
    dog = models.ForeignKey(Dog)
    date = models.DateField()
    in_office = models.BooleanField()

    class Meta:
        db_table = 'dogday'
