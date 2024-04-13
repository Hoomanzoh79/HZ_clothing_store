from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator
from django.template.defaultfilters import slugify
from multiselectfield import MultiSelectField as MSField

class MultiSelectField(MSField):
    """
    Custom Implementation of MultiSelectField to achieve Django 5.0 compatibility

    See: https://github.com/goinnn/django-multiselectfield/issues/141#issuecomment-1911731471
    """

    def _get_flatchoices(self):
        flat_choices = super(models.CharField, self).flatchoices

        class MSFFlatchoices(list):
            # Used to trick django.contrib.admin.utils.display_for_field into not treating the list of values as a
            # dictionary key (which errors out)
            def __bool__(self):
                return False

            __nonzero__ = __bool__

        return MSFFlatchoices(flat_choices)

    flatchoices = property(_get_flatchoices)


class Cloth(models.Model):
    CATEGORIES = [
        ('tshirt',_('tshirt')),
        ('pants',_('pants')),
        ('jacket',_('jacket')),
        ('suit',_('suit')),
        ('others', _('others')),
    ]

    SEASON_CHOICES = [('winter', _('winter')),
                      ('summer', _('summer')),
                       ('fall', _('fall')), 
                    ]
    
    GENDER_CHOICES = [('male', _('male')),
                      ('female', _('female')), 
                      ]
    
    SIZE_CHOICES = (
                    ('S', 'S'),
                    ('M', 'M'),
                    ('L','L'),
                    ('XL', 'XL'),
                    ('XXL', 'XXL'))
    
    sizes = MultiSelectField(choices=SIZE_CHOICES,
                             max_choices=6,
                             max_length=17,null=True)

    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=False,unique=True,allow_unicode=True)
    description = RichTextField(blank=True)
    price = models.PositiveIntegerField(validators=[MinValueValidator(50000)],default=0)
    season = models.CharField(max_length=6, choices=SEASON_CHOICES,blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    cover = models.ImageField(upload_to='cloth/cloth_covers', blank=True)
    sales = models.PositiveIntegerField(default=0,null=True)
    inventory = models.IntegerField(validators=[MinValueValidator(0)],default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES,null=True)
    brand = models.CharField(max_length=100,null=True)

    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("cloth_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def available_sizes(self):
        return tuple(self.sizes)
    
    def is_active(self,obj):
        return obj.inventory > 0


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    active = models.BooleanField(default=False)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.cloth}: {self.body}'

    # manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse("cloth_detail", kwargs={"slug": self.cloth.slug})