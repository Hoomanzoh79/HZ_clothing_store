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


class Color(models.Model):
    color_name = models.CharField(max_length=25)

    def __str__(self):
        return self.color_name

class Size(models.Model):
    size_name = models.CharField(max_length=5)

    def __str__(self):
        return self.color_name

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name
    
class Season(models.Model):
    season_name  = models.CharField(max_length=20)

    def __str__(self):
        return self.season_name

class Cloth(models.Model):
    GENDER_CHOICES = [('male', _('male')),
                      ('female', _('female')), 
                      ]
    
    sizes = models.ManyToManyField(Size,related_name="sizes")
    colors = models.ManyToManyField(Color,related_name="colors")
    categories = models.ManyToManyField(Category,related_name="categories")
    seasons = models.ManyToManyField(Season,related_name="seasons")

    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=False,unique=True,allow_unicode=True)
    description = RichTextField(blank=True)
    price = models.PositiveIntegerField(validators=[MinValueValidator(50000)],default=0,verbose_name=_("price"))
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,verbose_name=_("gender"))
    cover = models.ImageField(upload_to='cloth/cloth_covers', blank=True)
    sales = models.PositiveIntegerField(default=0,null=True)
    inventory = models.IntegerField(validators=[MinValueValidator(0)],default=0)
    brand = models.CharField(max_length=100,null=True,verbose_name=_("brand"))

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

    def available_colors(self):
        return tuple(self.colors.all())
    
    def is_active(self,obj):
        return obj.inventory > 0

    def hover_image(self):
        """returns the first value of cloth images as the hover image"""
        for file in self.images.all():
            return file.image

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


class Image(models.Model):
    cloth = models.ForeignKey(Cloth,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='cloth/cloth_covers',verbose_name='image')