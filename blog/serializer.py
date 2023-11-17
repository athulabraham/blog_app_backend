from rest_framework import serializers
from blog.models import BlogModel,UserModel

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogModel
        fields=(
            'title',
            'user_id',
            'post'
        )
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=(
            'name',
            'image',
            'email',
            'password'
        )