from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100,)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    dateCreated = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-dateCreated',)

    def commentCount(self):
        return self.comment_set.all().count()

    def comments(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200,)

    def __str__(self):
        return self.content