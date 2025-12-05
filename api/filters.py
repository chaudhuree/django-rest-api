#  add custom filter
import django_filters
from employees.models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(lookup_expr='iexact') # exact for exact match, iexact for case-insensitive match , icontains for case-insensitive contains
    emp_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Employee
        fields = ['designation','emp_name']