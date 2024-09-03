# form_extras.py
from django import template

register = template.Library()

@register.filter
def get_attr(form, field_name_and_index):
    field_name, index = field_name_and_index.split(' ')
    return form[field_name + index]