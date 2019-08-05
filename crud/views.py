from django.shortcuts import render,redirect
from crud.forms import CollegeForm
from crud.models import College



def create(request):

    form=CollegeForm()

    if request.method=='POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            clg=College()
            clg.clg_name = form.cleaned_data['clg_name']
            clg.clg_email = form.cleaned_data['clg_email']
            clg.clg_address = form.cleaned_data['clg_address']
            clg.save()
    return render (request,'clg/create.html',{'form':form})

def update(request):

    id=request.GET['id']
    data=College.objects.get(id=id)

    form = CollegeForm(instance=data)

    if request.method == 'POST':
        form = CollegeForm(request.POST,instance=data)
        if form.is_valid():
            clg = College()
            clg.id=id
            clg.clg_name = form.cleaned_data['clg_name']
            clg.clg_email = form.cleaned_data['clg_email']
            clg.clg_address = form.cleaned_data['clg_address']
            clg.save()

            return redirect(index)
    return render(request, 'clg/update.html', {'form': form})

def index(request):

    #select*from college
    resultSet=College.objects.all()
    #resultSet = College.objects.filter().values('id','clg_name','clg_email')  filter out certain datas
    return render(request,'clg/index.html',{'data':resultSet})

def delete(request):
    id=request.GET['id']
    data=College.objects.get(id=id)
    data.delete()
    return redirect(index)

def view(request):
    id=request.GET['id']
    resultInfo=College.objects.filter(id=id)

    return render(request,'clg/view.html',{'info':resultInfo})



