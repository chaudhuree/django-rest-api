from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def students(request):
    if request.method == 'GET':
        student_list = Student.objects.all()
        serializer = StudentSerializer(student_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)