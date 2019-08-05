from django.shortcuts import render

def helloDjango(request):

    d1={
        "name":"sandeep",
        "email":"sandeep@gmail.com",
        "list":[1,2,3,4,5,6],
        "d2":{"country":"USA" , "zip":"560012"}

    }
    return render(request, 'hello_django.html', d1)

def helloPython(request):
    return render(request, 'hello-python.html')
