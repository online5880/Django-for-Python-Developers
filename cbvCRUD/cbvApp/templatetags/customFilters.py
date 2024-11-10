from django import template
register=template.Library()


@register.filter(name='myLower')
def customLower(value):
    result=value[:3].lower()
    return result

@register.filter(name='myAppend')
def customAppend(value,arg):
    result = str(arg)+value
    return result

# register.filter("myLower",customLower)