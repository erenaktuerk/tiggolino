from tabnanny import verbose
from django.db import models

class Contact(models.Model):
  
    firstname = models.CharField(max_length=100, verbose_name='Firstname*')
    lastname = models.CharField(max_length=100, verbose_name='Lastname*')
    email = models.EmailField(verbose_name='Email*')
    tel = models.CharField(max_length=26, null=True,
                           blank=True, verbose_name='Phonenumber*')
    message = models.TextField(verbose_name='Message')
    inquiry_send_at_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Date')
    checked = models.BooleanField(default=False, verbose_name='Solved?')

    def __str__():
        return f'{self.lastname}s contact'





