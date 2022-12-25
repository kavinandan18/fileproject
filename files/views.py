from django.shortcuts import render
from .models import Employee
from .resources import EmployeeResource
from django.contrib import messages
from django.http import HttpResponse
from tablib import Dataset

def simple_upload(request):
    if request.method=="POST":
        emp_resource=EmployeeResource()
        dataset=Dataset()
        emp_data=request.FILES['myfiles']

        if not emp_data.name.endswith('xlsx'):
            messages.error(request,'Sorry Worng Format !! Please Upload .xlsx file')
            return render (request,'uploadfile.html')

        imported_data=dataset.load(emp_data.read(),format='xlsx')
        for data in imported_data:
            value=Employee(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4]
            )
            value.save()
        messages.info(request,'Your file Uploaded and Data Save into Database!!')
    return render (request,'uploadfile.html')
