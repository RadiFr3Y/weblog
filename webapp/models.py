from django.utils.html import format_html
from account.models import User
from django.urls import reverse
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment

class PostModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="images")
    STATUS_CHOICE = (
        ('p', 'published'),
        ('d', 'draft')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='d')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', default=User)
    comments = GenericRelation(Comment)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('account:home')

    def thumbnail_tag(self):
        return format_html('<img height="50" width="75" src="{}"'.format(self.thumbnail.url))
    

class WorkModel(models.Model):
    skills = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    github_url = models.CharField(max_length=100)
    about = models.TextField()
    image = models.ImageField(upload_to="work_img")

    def __str__(self):
        return self.skills


class Comment(models.Model):
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)