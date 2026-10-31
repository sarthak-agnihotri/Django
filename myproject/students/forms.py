from django import forms
class StudentForm(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    age=forms.IntegerField(min_value=18, max_value=60)