from django.shortcuts import render
# from .forms import StudentForm
from .forms import LoginForm

# def register(request):
#     form=StudentForm()
#     if request.method=="POST":
#         form=StudentForm(request.POST)
#         if form.is_valid():
#             name=form.cleaned_data['name']
#             email=form.cleaned_data['email']
#             age=form.cleaned_data['age']
#             return render(request,'students/success.html',{
#                 'name':name,
#                 'email':email,
#                 'age':age
#             })
#     return render(request,'students/register.html',{'form':form})

def login_view(request):
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            if username=="admin" and password=="admin123":
                return render(request,'students/welcome.html',{
                    'username':username
                })
            else:
                form.add_error(None,"Invalid username or password")
    return render(request,'students/login.html',{'form':form})
# Create your views here.
