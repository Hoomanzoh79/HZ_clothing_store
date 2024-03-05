from django import template

register = template.Library()


@register.filter
def only_recent_cloths(cloths):
    return cloths.filter(active=True).order_by("-datetime_created")


@register.filter
def only_female_cloths(cloths):
    return cloths.filter(active=True, gender="female").order_by("-datetime_created")


@register.filter
def only_male_cloths(cloths):
    return cloths.filter(active=True, gender="male").order_by("-datetime_created")
