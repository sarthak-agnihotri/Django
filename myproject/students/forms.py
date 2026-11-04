from django import forms
# class StudentForm(forms.Form):
#     name=forms.CharField(max_length=50)
#     email=forms.EmailField()
#     age=forms.IntegerField(min_value=18, max_value=60)

# class LoginForm(forms.Form):
#     username=forms.CharField(max_length=50)
#     password=forms.CharField(widget=forms.PasswordInput)

# class ContactForm(forms.Form):
#     name=forms.CharField(min_length=2,max_length=50)
#     email=forms.EmailField()
#     subject=forms.CharField(min_length=5,max_length=100)
#     message=forms.CharField(min_length=10,widget=forms.Textarea)

# class FeedbackForm(forms.Form):
#     name=forms.CharField(min_length=2,max_length=50)
#     email=forms.EmailField()
#     rating=forms.ChoiceField(
#         choices=[
#             ('1','1-Poor'),
#             ('2','2-Average'),
#             ('3','3-Good'),
#             ('4','4-Very Good'),
#             ('5','5-Excellent')
#         ]
#     )
#     feedback=forms.CharField(min_length=10,widget=forms.Textarea)

class ValidationForm(forms.Form):
    name=forms.CharField(min_length=3,max_length=50)
    email=forms.EmailField()
    age=forms.IntegerField(min_value=10,max_value=60)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    #name validation
    def clean_name(self):
        name=self.cleaned_data['name']
        if not name.isalpha():
            raise forms.ValidationError("Name can only contain letters")
        return name
    #email validation
    def clean_email(self):
        email=self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email must be a Gmail address")
        return email
    #age validation
    def clean_age(self):
        age=self.cleaned_data['age']
        if age<18:
            raise forms.ValidationError("Age must be at least 18")
        return age
    #password validation
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        if password and confirm_password and password!=confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
    
