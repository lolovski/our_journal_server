from django import template


register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})
register.filter('addclass', addclass)


@register.filter
def in_category(field, category):
    return field.filter(week=category)


@register.filter
def remainder_by_10_equally_0(field):
    return field % 10 == 0 and field != 0


@register.filter
def division_by_10(field):
    return field // 10 + 1


@register.filter
def index_list(field, index):
    return field[index // 10]


