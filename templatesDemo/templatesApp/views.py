from django.shortcuts import render

# Create your views here.

def renderTemplate(request):
    myDict={"name":"mane"}
    return render(request,"templatesApp/firstTemplate.html",context=myDict)

def renderEmployee(request):
    myDic={"id":123, "name":"Park","sal":10000}
    return render(request, "templatesApp/employeeTemplate.html",myDic)