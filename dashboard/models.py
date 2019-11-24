from django.db import models

# The Compaign model
class Compaign(models.Model):
    date =  models.DateField()
    data_source = models.CharField(max_length=200)
    compaign_name = models.CharField(max_length=200)
    clicks = models.DecimalField(decimal_places=0, max_digits=10, blank=True)
    impressions = models.DecimalField(decimal_places=1, max_digits=10, blank=True, null=True)