from django.db import models
from django.contrib.auth.models import User
from PIL import Image




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')
    distrito = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    cidade = models.CharField(max_length=250, default= " ")
    pnome = models.CharField(max_length=250, default= " ")
    snome = models.CharField(max_length=250, default= " ")
    NSID = models.CharField(max_length=250, default= " ")

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
