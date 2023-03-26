from django.db import models


class Cloths(models.Model):
    SEASON_CHOICES = [('winter', 'winter'),
                       ('summer', 'summer'),
                       ('fall', 'fall'), ]
    GENDER_CHOICES = [('male', 'male'),
                      ('female', 'female'), ]

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(default=True)
    active = models.BooleanField(default=True)
    season = models.CharField(max_length=6, choices=SEASON_CHOICES)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


