from django import template
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.inclusion_tag('likeable/badge.html', takes_context=True)
def likeable_badge(context, obj):
    content_type = ContentType.objects.get_for_model(obj)
    uri = reverse('likeable_like', kwargs={'content_type_id': content_type.id, 'object_id': obj.id })
    liked = obj.likes.filter(user=context['request'].user).exists()
    return {
        'uri': uri,
        'counter': obj.likes.count(),
        'liked': liked
    }

