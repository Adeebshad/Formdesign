from django.db import models

# Create your models here.
from django.core.files.base import File

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name

    def image_img(self):
        if self.file:
            return u'<img src="%s" width="50" height="50" />' % self.item_image.url
        else:
            return '(Sin imagen)'
        image_img.short_description = 'Thumb'
        image_img.allow_tags = True