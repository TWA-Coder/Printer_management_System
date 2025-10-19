from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, PrinterViewSet, UserViewSet, create_print_job

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'printers', PrinterViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('v1/print-jobs/', create_print_job, name='create_print_job'),
    path('', include(router.urls)),
]
