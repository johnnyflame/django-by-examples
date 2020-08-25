from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    # the widget ensures the HTML treats this field as a password input (i.e, blocked out from plainview)
    password = forms.CharField(widget=forms.PasswordInput)

