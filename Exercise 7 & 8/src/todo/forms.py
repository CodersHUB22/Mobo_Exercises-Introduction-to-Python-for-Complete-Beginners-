from django import forms


class TodoForm(forms.Form):
    id = forms.IntegerField()
    todo_text = forms.CharField()
