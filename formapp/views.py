from django.shortcuts import render
from formapp.forms import UserProfileForm

def userProfile(request):

    #print(request.GET)


    obj=UserProfileForm()

#validation

    if request.method=='POST':
        obj=UserProfileForm(request.POST)  #passing the data
        if obj.is_valid():
            pass

    return render(request, 'user_profile.html', {'form':obj} )
