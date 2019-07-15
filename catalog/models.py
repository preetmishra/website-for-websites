from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model) :
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('NA', 'Prefer not to say'),
    )
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    gender = models.CharField(max_length = 2, choices = GENDER)
    profile_picture = models.ImageField(upload_to = 'profile_pictures', blank = True)

    def __str__(self) :
        return self.user.username

class Tag(models.Model) :
    tag = models.CharField(max_length = 30)
    
    def __str__(self) :
        return self.tag

class Website(models.Model) :

    def default_user() :
        return User.objects.get(username='Anon').pk

    name = models.CharField(max_length = 128)
    url = models.URLField()
    description = models.CharField(max_length=256, blank=True, default='')
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE, related_name = 'tags')
    user = models.ForeignKey(User, on_delete = models.SET_DEFAULT, default = default_user)
    date_added = models.DateTimeField(default = timezone.now)
    
    def __str__(self) :
        return self.name

class UserAndWebsite(models.Model) :
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    website = models.ForeignKey(Website, on_delete = models.CASCADE)

    def __str__(self) :
        return self.user.username + ' has ' + self.website.name
