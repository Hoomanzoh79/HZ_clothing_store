from django import template
register = template.Library()


@register.filter
def translate_number(value):
    value = str(value)
    english_to_persian_table = str.maketrans('0123456789', '۰١٢٣٤٥٦٧٨٩')
    return value.translate(english_to_persian_table)