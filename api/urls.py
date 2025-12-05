from django.urls import path,include
from . import views
# viewsets
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('employees', views.EmployeesViewSet)

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

        # blogs
    path('blogs/', views.BlogsView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),

    path('comments/', views.CommentView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]