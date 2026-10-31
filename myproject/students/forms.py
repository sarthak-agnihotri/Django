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

class FeedbackForm(forms.Form):
    name=forms.CharField(min_length=2,max_length=50)
    email=forms.EmailField()
    rating=forms.ChoiceField(
        choices=[
            ('1','1-Poor'),
            ('2','2-Average'),
            ('3','3-Good'),
            ('4','4-Very Good'),
            ('5','5-Excellent')
        ]
    )
    feedback=forms.CharField(min_length=10,widget=forms.Textarea)