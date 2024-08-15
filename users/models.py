from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField("nombre del usuario",max_length=50)
    last_name = models.CharField("apellidos del usuario",max_length=50)
    car = models.ManyToManyField('Car', verbose_name="los carros del usuario")

STATUS_CHOICES = {
    ('R', 'Reviewed'),
    ('N', 'Not Reviewed'),
    ('E', 'Error'),
    ('A', 'Accepted')
}

class Website (models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField( max_length=200)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Car(models.Model):
    name = models.CharField( max_length=50, primary_key=True)