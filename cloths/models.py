from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


class Cloth(models.Model):
    SEASON_CHOICES = [('winter', 'winter'),
                       ('summer', 'summer'),
                       ('fall', 'fall'), ]
    GENDER_CHOICES = [('male', 'male'),
                      ('female', 'female'), ]
    
    SIZE_CHOICES = (('XXS', 'XXS'),
                    ('XS', 'XS'),
                    ('S', 'S'),
                    ('M', 'M'),
                    ('XL', 'XL'),
                    ('XXL', 'XXL'))
    
    sizes = MultiSelectField(choices=SIZE_CHOICES,
                             max_choices=6,
                             max_length=17,null=True)

    title = models.CharField(max_length=50)
    description = RichTextField(blank=True)
    price = models.PositiveIntegerField(default=True)
    active = models.BooleanField(default=True)
    season = models.CharField(max_length=6, choices=SEASON_CHOICES)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    cover = models.ImageField(upload_to='cloth/cloth_covers', blank=True)

    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cloth_detail', args=[self.id])


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cloth}: {self.body}'

    # manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('cloth_detail', args=[self.cloth.id])


