from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=30)

    class Meta:
        ordering = ('tag',)

    def __str__(self):
        return self.tag

class Website(models.Model):

    def default_user():
        return User.objects.get(username='Anon').pk

    name = models.CharField(max_length=128, verbose_name='title', unique=True)
    url = models.URLField(help_text='Do not forget to add http:// or https://.')
    description = models.CharField(max_length=256, blank=True, default='')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tags')
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=default_user)
    date_added = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default='False')

    def __str__(self):
        return self.name

class Profile(models.Model) :
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('NA', 'Prefer not to say'),
    )
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    gender = models.CharField(max_length = 2, choices = GENDER)
    profile_picture = models.ImageField(upload_to = 'profile_pictures', default = 'default.png')
    favourites = models.ManyToManyField(Website, related_name = 'favourited_by')

    @classmethod
    def add_or_remove_favourites(cls, user_id, website_id, operation) :
        profile = Profile.objects.get(user = user_id)
        if operation == 'add' :
            profile.favourites.add(website_id)
        elif operation == 'remove' :
            profile.favourites.remove(website_id)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300 :
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)

    
    def __str__(self) :
        return self.user.username
