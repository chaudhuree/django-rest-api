from rest_framework import serializers
from .models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    blog_title = serializers.CharField(source='blog.blog_title', read_only=True)
    blog_url = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'created_at', 'updated_at', 'blog_title', 'blog_url']
        depth = 0

    def get_blog_url(self, obj):
        # adjust base path to your real blog endpoint
        request = self.context.get('request')
        if request is not None:
            # build absolute URL: http://host/api/v1/blogs/<id>/
            return request.build_absolute_uri(f'/api/v1/blogs/{obj.blog.id}/')
        # fallback (relative)
        return f'/api/v1/blogs/{obj.blog.id}/'


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'