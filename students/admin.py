from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'branch', 'roll')
    list_per_page = 10
    search_fields = ('student_id', 'name', 'branch', 'roll')

    # def get_queryset(self, request):
    #     return super().get_queryset(request).order_by('student_id')
    
    # def get_list_display(self, request):
    #     return ('student_id', 'name', 'branch', 'roll')