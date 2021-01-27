from django_filters import FilterSet, filters

from django.db.models import Q

from users.models import User


class UserFilter(FilterSet):
    name = filters.CharFilter(field_name="name", label="name", lookup_expr="icontains")
    email = filters.CharFilter(
        field_name="email", label="email", lookup_expr="icontains"
    )
    school = filters.CharFilter(method="school_search", label="school", required=True)

    class Meta:
        model = User
        fields = ["user_type"]

    def school_search(self, queryset, name, value):
        return queryset.filter(
            Q(student__school__id=value)
            | Q(parent__students__school__id=value)
            | Q(teacher__school__id=value)
            | Q(school__id=value)
        )