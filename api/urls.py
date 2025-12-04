from django.urls import path,include
from . import views
# viewsets
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'employees', views.EmployeesViewSet)

urlpatterns = [
    # function based views
    path('students/',views.students),
    path('students/<int:id>/',views.student),

    # class based views
    # mixins, generics
    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>/',views.Employee_Details.as_view()),
    
    # viewsets
    path('', include(router.urls)),
]