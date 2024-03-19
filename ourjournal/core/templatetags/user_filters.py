from django import template


register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})
register.filter('addclass', addclass)

@register.filter
def in_category(field, category):
    return field.filter(week=category)


