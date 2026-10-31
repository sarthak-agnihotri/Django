from django.shortcuts import render,redirect
from django.contrib import messages
# from .forms import StudentForm
# from .forms import LoginForm
# from .forms import ContactForm
from .forms import FeedbackForm

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

# def login_view(request):
#     form=LoginForm()
#     if request.method=="POST":
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password']
#             if username=="admin" and password=="admin123":
#                 return render(request,'students/welcome.html',{
#                     'username':username
#                 })
#             else:
#                 form.add_error(None,"Invalid username or password")
#     return render(request,'students/login.html',{'form':form})

# def contact(request):
#     form=ContactForm()
#     if request.method=="POST":
#         form=ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             messages.success(request,"Thank you for contacting us!")
#             return redirect('success')
#     else:
#         return render(request,"students/contact.html",{'form':form})

# def success(request):
#     return render(request,"students/success.html")

def feedback(request):
    form=FeedbackForm()
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            rating=form.cleaned_data['rating']
            feedback=form.cleaned_data['feedback']
            return redirect('success')
    else:
        return render(request,'students/feedback.html',{'form':form})
def success(request):
    return render(request,'students/success.html')
# Create your views here.
