from django import template

register = template.Library()


@register.simple_tag(name='getstatus')

def getstatus(status):
    status=status-1
    status_array=['CONFIRMED','PROCESSED','DELIVERED','REJECTED']
    return status_array[status]
    
      
