from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.utils.translation import gettext_lazy as _

# Create your models here.



def avatar_preview_directory_path(instance: "Profile", filename: str) -> str:
    return "profiles/profile_{pk}/avatar/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )

class Profile(models.Model):
    class Meta:
        verbose_name_plural = _("profile")
        verbose_name = _('profiles')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))
    bio = models.TextField(max_length=500, blank=True, verbose_name=_('bio'))
    agreement_accepted = models.BooleanField(default=False, verbose_name=_('agreement_accepted'))
    avatar = models.ImageField(default='default.jpg', null=True, blank=True, upload_to=avatar_preview_directory_path, verbose_name=_('avatar'))

    def __str__(self):
        return f'{self.user.username}'


    def save(self):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

