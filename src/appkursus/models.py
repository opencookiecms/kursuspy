from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    course_name = models.CharField(max_length=200, null=True, blank=True)
    course_startdate = models.CharField(max_length=12, null=True, blank=True)
    course_endate = models.CharField(max_length=12, null=True, blank=True)
    course_place = models.CharField(max_length=12, null=True, blank=True)
    course_year = models.CharField(max_length=8, null=True, blank=True)
    course_days = models.CharField(max_length=20, null=True, blank=True)
    course_by = models.CharField(max_length=200, null=True, blank=True)

class Attandance(models.Model):
    dayone = models.CharField(max_length=5, null=True, blank=True)
    daytwo = models.CharField(max_length=5, null=True, blank=True)
    daythree = models.CharField(max_length=5, null=True, blank=True) 
    dayfour = models.CharField(max_length=5, null=True, blank=True)
    dayfive = models.CharField(max_length=5, null=True, blank=True)
    daysix = models.CharField(max_length=5, null=True, blank=True)
    dayseven = models.CharField(max_length=5, null=True, blank=True)
    dayeight = models.CharField(max_length=5, null=True, blank=True)
    daynine = models.CharField(max_length=5, null=True, blank=True)
    dayten = models.CharField(max_length=5, null=True, blank=True)
    cid = models.ForeignKey(Course, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)

class UnitGroup(models.Model):
    unitname = models.CharField(max_length=50, null=True, blank=True)

class Sokongan(models.Model):
    sokonganname = models.CharField(max_length=50, null=True, blank=True)

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nobadan = models.CharField(max_length=50, null=True, blank=True)
    gambar = models.FileField(null=True, blank=True);
    nokp = models.CharField(max_length=50, null=True, blank=True)
    balaioperasi = models.CharField(max_length=50, null=True, blank=True) 
    jawatan = models.CharField(max_length=50, null=True, blank=True)
    gredjawatan = models.CharField(max_length=50, null=True, blank=True)
    unitsokongan  = models.ForeignKey(Sokongan, on_delete=models.CASCADE)
    groupunit = models.ForeignKey(UnitGroup, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name



    



# Create your models here.
