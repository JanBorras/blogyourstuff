from django.db import models
from accounts.models import UserProfile

class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
