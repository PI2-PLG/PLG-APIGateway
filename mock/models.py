from django.db import models

# Create your models here.
class Mock(models.Model)

    class Meta:

        db_table = 'mock'

        module_name = models.CharField(max_length=200)
        temperature = models.DecimalField(decimal_places=2,max_digits=3)
        co2 = modes.DecimalField(decimal_places=2,max_digits=10)
        humidity = modes.DecimalField(decimal_places=2,max_digits=10)
        latitude = models.CharField(max_length=200)
        longitude = models.CharField(max_length=200)