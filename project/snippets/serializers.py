from rest_framework import serializers
from project.snippets.models import Snippet, User, Articles, Comments, UserTags, ArticleTags


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
       model = User
       fields = ('id', 'name', 'age', 'email', 'gender','eduLevel')



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
       model = Articles
       fields = ('title', 'url', 'paper', 'author', 'date', 'time', 'description')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
       model = Comments
       fields = ('text', 'articleID', 'userID', 'date', 'time')


class UserTagSerializer(serializers.ModelSerializer):
    class Meta:
       model = UserTags
       fields = ('tag', 'frequency', 'userID')


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
       model = ArticleTags
       fields = ('tag', 'articleID')
