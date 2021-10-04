from rest_framework import serializers
from django.apps import apps

Post = apps.get_model('blog', 'Post')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')
        model = Post