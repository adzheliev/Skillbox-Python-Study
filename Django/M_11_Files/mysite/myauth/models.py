from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Create your models here.



def avatar_preview_directory_path(instance: "Profile", filename: str) -> str:
    return "profiles/profile_{pk}/avatar/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    agreement_accepted = models.BooleanField(default=False)
    avatar = models.ImageField(default='default.jpg', null=True, blank=True, upload_to=avatar_preview_directory_path)

    def __str__(self):
        return '%s %s' % (self.user.name)




    def save(self):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

