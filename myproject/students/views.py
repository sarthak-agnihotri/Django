from django.shortcuts import render
from .forms import StudentForm

def register(request):
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            age=form.cleaned_data['age']
            return render(request,'students/success.html',{
                'name':name,
                'email':email,
                'age':age
            })
    return render(request,'students/register.html',{'form':form})
# Create your views here.
