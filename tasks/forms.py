from django import forms
from.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important'] # crear formulario a partir de los datos de una tabla
        widgets = {
            'title': forms.TextInput(attrs={'class': 'formcontrol', 'placeholder': 'Title of the task'}),
            'description': forms.Textarea(attrs={'class': 'formcontrol', 'placeholder': 'write something' }),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }
