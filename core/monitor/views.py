from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Department, Printer, PrintJob
from .serializers import DepartmentSerializer, PrinterSerializer, UserSerializer, PrintJobSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PrinterViewSet(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def create_print_job(request):
    data = request.data
    try:
        printer = Printer.objects.get(printer_id=data.get('printer_id'))
        user = User.objects.get(email=data.get('user_email'))
    except Printer.DoesNotExist:
        return Response({'error': 'Printer not found'}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    department = printer.department
    pages = data.get('pages_printed')

    job = PrintJob.objects.create(
        user=user,
        printer=printer,
        department=department,
        pages_printed=pages,
        is_duplex=data.get('is_duplex', False)
    )
    serializer = PrintJobSerializer(job)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

