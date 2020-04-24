from django.db import models

# Create your models here.

# stores client info and score
class Member(models.Model):
	name = models.CharField(max_length=300)
	tag_UID = models.CharField(max_length=16, blank=True)
	email = models.EmailField(max_length=254)
	score = models.IntegerField(blank=True)
	img = models.ImageField(upload_to=create_upload_url, blank=True)
	PAWS_ID = models.CharField(max_length=6)


def create_upload_url(instance, filename):
	return 'usr/{0}'.format(filename)
