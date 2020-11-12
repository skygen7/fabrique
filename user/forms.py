from django import forms


class UserName(forms.Form):
    name = forms.CharField(max_length=100, required=False)
