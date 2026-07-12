from django import template

register = template.Library()

HOUSE_SLUGS = {'gryffindor', 'slytherin', 'hufflepuff', 'ravenclaw'}


@register.filter
def house_slug(name):
    """Map a house name to one of the four known CSS accent classes, falling back to a neutral default."""
    slug = (name or '').strip().lower()
    return slug if slug in HOUSE_SLUGS else 'default'
