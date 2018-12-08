from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #website = models.URLField(blank=True)
    # Comentei isso aqui e deu pau
    picture = models.ImageField(upload_to='profile_images', blank=True) # trocar aqui para icones de linux

    def __str__(self):
        return self.user.username