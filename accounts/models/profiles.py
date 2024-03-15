from django.db import models
from .users import CustomUser
from django.core.validators import RegexValidator

class Profile(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=12, 
                                    validators=[RegexValidator(regex="^[0][9][0-9][0-9]{8,8}$")],
                                    blank=True,)
    email = models.EmailField(max_length=255, unique=True,blank=True)

    def __str__(self):
        return f'profile : {self.user.username}'