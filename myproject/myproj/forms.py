from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    age=forms.IntegerField(min_value=18,max_value=60)
    course=forms.ChoiceField(
    choices=[
        ('python','python'),
        ('BTECH','BTECH'),
        ('MCA','MCA'),
    ])

# class MyForm(forms.Form):
#     name = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
#     )