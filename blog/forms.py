from django import forms
from blog.models import BlogComment
from captcha.fields import CaptchaField



class CommentForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = BlogComment
        fields = "__all__"