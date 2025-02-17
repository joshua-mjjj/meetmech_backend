from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


SERVICE_TYPES = (
    ('wiring', 'Car wiring'),
    ('alignment', 'Wheel Alignment'),
    ('electrics', 'Electric Cars'),
    ('engines', 'Engine Checking'),
    ('wheel_balancing', 'Wheel Balancing'),
    ('flat_tyres', 'Flat Tyres'),
    ('computer_aided_mechanics', 'Computer Aided Mechanics'),

)

LOCATIONS = (
    ('kampala', 'Kampala'),
    ('kayinga', 'Kayinga'),
    ('kakiri', 'Kakiri'),
    ('Nsambya', 'Nsambya'),
    ('Entebbe', 'Entebbe'),
    ('Munyonyo', 'Munyonyo'),
    ('Kiboga', 'Kiboga'),
    ('Mityana', 'Mityana'),
    ('Lugazi', 'Lugazi'),
    ('Kamuli', 'Kamuli'),
    ('Iganga', 'Iganga'),
    ('Kitgum', 'Kitgum'),
    ('Mbarara', 'Mbarara'),
    ('Gulu', 'Gulu'),
)



class Status(models.Model):
	status = models.CharField(max_length=50)
	owner_username =  models.CharField(max_length=32, blank=True)
	user   = models.ForeignKey(
			    User, related_name="statuses", 
			    on_delete=models.CASCADE, null=True)

	def __str__(self):
		return '{}'.format(self.user)


class Client(models.Model):
	service  = models.CharField(max_length=150)
	Location = models.CharField(max_length=150)

	def save(self, *args, **kwargs):
		super(Client, self).save(*args, **kwargs)

	def __str__(self):
		return '{}'.format(self.service)

class serviceProvider(models.Model):
	service  = models.CharField(max_length=32, choices=SERVICE_TYPES, blank=True)
	owner_username =  models.CharField(max_length=100, blank=True)
	location = models.CharField(max_length=32, choices=LOCATIONS, blank=True)
	name     = models.CharField(max_length=100, null=False ,blank=False)
	photo = models.FileField(upload_to="media/photos/service_provider_avatars/", blank=True)
	contact  = models.CharField(max_length=105, null=False ,blank=False)
	email    = models.EmailField(max_length=100, null=True,blank=True)
	other    = models.CharField(max_length=10000)
	#profile_picture = models.ImageField(blank=True, null=True, upload_to=upload_path)
	owner    = models.ForeignKey(
	    User, related_name="profiles", 
	    on_delete=models.CASCADE, null=True)

	def __str__(self):
		return '{}'.format(self.owner)




# Please don't mind this model and its serializers and views, i was jus using it for some other stuff
class Note(models.Model):
	createDateTime      = models.IntegerField(default=datetime.now().date())
	lastEditDateTime    = models.IntegerField(default=datetime.now().time())
	noteTitle           = models.CharField(max_length=150)
	noteDescription     = models.CharField(max_length=150)

	def save(self, *args, **kwargs):
		super(Note, self).save(*args, **kwargs)

	def __str__(self):
		return '{}'.format(self.noteTitle)


