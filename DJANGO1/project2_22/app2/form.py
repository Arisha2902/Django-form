from django import forms

class Empforms(forms.Form):
    name=forms.CharField(max_length=100)
    branch=forms.CharField(max_length=100)