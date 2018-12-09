from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # Invés de imagens de perfil posso fazer um model só para forms
    # e colocar as imagens no index, como de icones de distribuição linux

    def __str__(self):
        return self.user.username