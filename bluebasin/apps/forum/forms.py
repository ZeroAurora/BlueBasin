from django import forms


class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    content = forms.CharField(max_length=10000, required=True)


class ReplyPostForm(forms.Form):
    content = forms.CharField(max_length=10000, required=True)
