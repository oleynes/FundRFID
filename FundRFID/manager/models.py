from django.db import models
from .validators import validate_pawsid

# Create your models here.
CLASS_YEAR = [
	('FR', 'Freshman'),
	('SO', 'Sophomore'),
	('JR', 'Junior'),
	('SR', 'Senior'),
	('SS', 'Super Senior'),
	('GR', 'Graduate'),
	('AL', 'Alumni')
]


def create_upload_url(instance, filename):
	return 'usr/{0}'.format(filename)


# stores client info and score
class Member(models.Model):
	name = models.CharField(max_length=300)
	tag_UID = models.CharField(max_length=16, blank=True, verbose_name='Tag UID')
	email = models.EmailField(max_length=254)
	score = models.IntegerField(default=0)
	img = models.ImageField(upload_to=create_upload_url, blank=True, verbose_name='Member Image')
	PAWS_ID = models.IntegerField(verbose_name='PAWS ID', primary_key=True, validators=[validate_pawsid])
	class_year = models.CharField(max_length=2, choices=CLASS_YEAR, default='FR')




