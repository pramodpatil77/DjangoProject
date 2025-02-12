from rest_framework import generics
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .serializers import EmployeeSerializer
from .forms import EmployeeForm

# DRF API Views
class EmployeeListCreate(generics.ListCreateAPIView):
    """API endpoint to list all employees or create a new employee."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint to retrieve, update, or delete a specific employee."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Django Views
def home(request):
    """Renders the homepage."""
    return render(request, 'home.html')

def view_records(request):
    """Displays the list of all employees."""
    employees = Employee.objects.all()
    return render(request, 'view_records.html', {'employees': employees})

def add_employee(request):
    """Handles adding a new employee."""
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_records')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def edit_employee(request, pk):
    """Handles editing an existing employee."""
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('view_records')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})

def delete_employee(request, pk):
    """Handles deleting an employee."""
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('view_records')
    return render(request, 'delete_employee.html')
