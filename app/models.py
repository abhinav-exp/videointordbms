from django.db import models
from django.core.files.base import File

# Create your models here.
class VideoModel(models.Model):
    np_field = models.FileField()

    # def save(self, *args, **kwargs):
    #     super().save(*args,**kwargs)
    #     with open(r'testviedo.mp4' , encoding="utf8", errors='ignore') as f:
    #         self.np_field.save('hello.mp4', File(f))
    #     print("save called")

import base64

from django.db import models

class Foo(models.Model):

    id = models.AutoField(primary_key=True)

    _data = models.BinaryField(
            db_column='data',
            blank=True)

    def set_data(self, data):
        self._data = base64.encodestring(data)

    def get_data(self):
        return base64.decodestring(self._data)

    data = property(get_data, set_data)

        