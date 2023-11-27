from django import forms


class InfoSettingsForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True)
    phone = forms.CharField(max_length=11, required=True)


class PasswordSettingsForm(forms.Form):
    old_password = forms.CharField(max_length=100, required=True)
    new_password = forms.CharField(max_length=100, required=True)
    confirm_password = forms.CharField(max_length=100, required=True)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=100)
    confirm_password = forms.CharField(max_length=100)
