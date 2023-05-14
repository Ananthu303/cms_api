from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField(null=True,blank=True)
    content=models.TextField(null=True,blank=True)
    creation_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=200,default='Public')
    def likes_count(self):
       return self.likes.all().count()
    def username(self):
        return self.user.username
    
    
    def __str__(self):
        return self.title

   
class Likes(models.Model):
    post=models.ForeignKey(Post,on_delete=models.SET_NULL,null=True,related_name='likes')
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def username(self):
        return self.user.username
    def p(self):
        return self.post
    

    def __str__(self):
        return self.user.username
    