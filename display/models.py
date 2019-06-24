from django.db import models

# Create your models here.
class Plane(models.Model):
    color = models.CharField(max_length=100)
    nnumber = models.CharField(max_length=100)
    lasttach = models.CharField(max_length=100)
    currenttach = models.CharField(max_length=100)
    lastflight = models.CharField(max_length=100)
    recordsreview = models.CharField(max_length=100)
    annualdue = models.CharField(max_length=100)
    fiftyhourdue = models.CharField(max_length=100)
    hundredhourdue = models.CharField(max_length=100)
    transponderdue = models.CharField(max_length=100)
    phaseone = models.CharField(max_length=100)
    phasetwo = models.CharField(max_length=100)
    phasethree = models.CharField(max_length=100)
    phasefour = models.CharField(max_length=100)
    aircraftstatus = models.CharField(max_length=100)
    discrepancies = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nnumber)



class Pilot(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    cert = models.CharField(max_length=100)
    certnumber = models.CharField(max_length=100)
    medicaldue = models.CharField(max_length=100)
    medicalclass = models.CharField(max_length=100)
    faase = models.CharField(max_length=100)
    faame = models.CharField(max_length=100)
    faainst = models.CharField(max_length=100)
    faainsttype = models.CharField(max_length=100)
    opsapproved = models.CharField(max_length=100)
    acapproved = models.CharField(max_length=100)
    daycurrency = models.CharField(max_length=100)
    nightcurrency = models.CharField(max_length=100)
    checkairman = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name) + ", " + str(self.title)
