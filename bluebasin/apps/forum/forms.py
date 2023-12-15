from django import forms

from bluebasin.apps.admin.models import Report

class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    content = forms.CharField(max_length=10000, required=True)


class ReplyPostForm(forms.Form):
    content = forms.CharField(max_length=10000, required=True)

class ReportPostForm(forms.Form):
    type = forms.TypedChoiceField(choices=Report.Type.choices, coerce=int, required=True)
    detail = forms.CharField(max_length=10000, required=True)
