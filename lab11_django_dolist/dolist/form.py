from django import forms

class todolistform(forms.form):
    test = forms.CharField(max_length=45, widget=forms.TextInput(attrs={'class','todo_text','placeholder': 'type your task...','aria-label':'task','aria-describeby':'btn-add'}))