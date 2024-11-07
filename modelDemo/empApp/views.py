from django.shortcuts import render
from empApp.models import Employee
# Create your views here.
def employeedata(request):
    # SELECT * FROM Employee
    employee = Employee.objects.all()
    empDict = {'employees':employee}
    return render(request,'./empApp/employees.html',empDict)