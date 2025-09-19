from django.db import models
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User

# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2,"Archived"),
)

class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    lead = models.CharField(max_length=600)
    category = models.ManyToManyField(BlogCategory)
    author = models.ForeignKey(User, on_delete= models.SET_NULL,related_name='blog_posts',null=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_images/",default="blog_images/default.png")
    updated_on = models.DateTimeField(auto_now= True)
    created_on = jmodels.jDateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    view_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_on']

