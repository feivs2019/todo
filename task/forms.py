from django import forms
from .models import *

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("task","author",)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["task"].label = "task"
        self.fields["author"].label = "author"
        # CreateViewからのみuserが渡される
        if "user" in kwargs:
            self.fields["author"].initial = kwargs["user"]
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-task'
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs['id'] = field.label


