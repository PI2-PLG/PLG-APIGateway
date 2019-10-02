from django.db import models

# Create your models here.
class Mock(models.Model):

    class Meta:

        db_table = 'mock'

    module_name = models.CharField(max_length=200)
    temperature = models.DecimalField(decimal_places=2,max_digits=5)
    co2 = models.DecimalField(decimal_places=2,max_digits=12)
    humidity = models.DecimalField(decimal_places=2,max_digits=12)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)