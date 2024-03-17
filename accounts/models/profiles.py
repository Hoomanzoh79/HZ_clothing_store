from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

from .users import CustomUser


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50,blank=True,verbose_name=_('First name'))
    last_name = models.CharField(max_length=50,blank=True,verbose_name=_('Last name'))
    address = models.TextField(blank=True,verbose_name=_('Address'))
    phone_number = models.CharField(max_length=12, 
                                    validators=[RegexValidator(regex="^[0][9][0-9][0-9]{8,8}$")],
                                    blank=True,verbose_name=_('Phone number'))

    def __str__(self):
        return f'profile : {self.user.username}'
