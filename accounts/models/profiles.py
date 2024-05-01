from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
from django.utils import timezone

from .users import CustomUser


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50,blank=True,verbose_name=_('First name'))
    last_name = models.CharField(max_length=50,blank=True,verbose_name=_('Last name'))
    address = models.TextField(blank=True,verbose_name=_('Address'))
    postal_code = models.CharField(max_length=10,
                                validators=[RegexValidator(regex="^(?!(\d)\1{3})[13-9]{4}[1346-9][ -]?[013-9]{5}$|^$")],
                                verbose_name=_("Postal code"),null=True
                                )
    phone_number = models.CharField(max_length=12, 
                                    validators=[RegexValidator(regex="^[0][9][0-9][0-9]{8,8}$")],
                                    blank=True,verbose_name=_('Phone number'))
    
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'profile : {self.user.username}'
