from django.urls import path
from . import views
urlpatterns = [
    # class based views
    path('employees/',views.Employees.as_view()),
    path('employees/<int:pk>/',views.Employee_Details.as_view()),
]