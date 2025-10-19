from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Department(models.Model):
    name = models.CharField(max_length=100)
    paper_quota = models.IntegerField(help_text="Number of sheets per month")

    def __str__(self):
        return self.name


class Printer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    printer_id = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class PrintJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    pages_printed = models.IntegerField()
    is_duplex = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.pages_printed} pages"

