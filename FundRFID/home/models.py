from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    dt = models.DateTimeField()
    description = models.TextField()
    img = models.ImageField(blank=True, upload_to='events/images/')

    def has_img(self):
        return self.img is not None


class Announcement(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    img = models.ImageField(blank=True, upload_to='announcements/images/')
    post_date = models.DateTimeField(auto_now=True)

    def has_img(self):
        return self.img is not None


class EboardMember(models.Model):
    POSITIONS = [
        ('0', 'President'),
        ('1', 'Vice President'),
        ('2', 'Treasurer'),
        ('3', 'Secretary'),
        ('6', 'Fundraising Chair'),
        ('7', 'Event\'s Coordinator'),
        ('8', 'Mystique Chair'),
        ('4', 'Publicist'),
        ('5', 'Historian'),
        ('9', 'Freshman Rep.'),
    ]

    CLASS_YEAR = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('SS', 'Super Senior'),
        ('GR', 'Graduate'),
    ]
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    position = models.CharField(choices=POSITIONS, max_length=2, default='FR')
    profile = models.ImageField(default='util/blank_profile.png', upload_to='eboard/images/')
    email = models.EmailField()
    class_year = models.CharField(choices=CLASS_YEAR, max_length=2, default='FR')

    def has_img(self):
        return self.profile is not None
