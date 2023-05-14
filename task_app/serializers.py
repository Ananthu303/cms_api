from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email','password']

    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields  = ["id","user","username", "title","description","content","creation_date", "likes_count","status",] 


class Likeserializer(serializers.ModelSerializer):
    class Meta:
        model=Likes
        fields=["post","user","username"] 

  