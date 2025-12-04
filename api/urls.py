from django.urls import path
from . import views
urlpatterns = [
    # function based views
    path('students/',views.students),
    path('students/<int:id>/',views.student),

    # class based views
    path('employees/',views.Employees.as_view()),
    path('employees/<int:id>/',views.Employee_Details.as_view()),
]