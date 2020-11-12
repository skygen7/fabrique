from django import forms
from .models import Questions


class Answer(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ('title',)
