from django.forms import ModelForm
from blog.models import BlogComment


class BlogCommentForm(ModelForm):
    class Meta:
        model = BlogComment
        fields = '__all__'