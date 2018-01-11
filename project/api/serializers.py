from django.contrib.auth.models import User
from django.contrib.auth.models import GroupManager
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')





class DerrickSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupManager
        fields = ('url', 'groupname', 'email', 'users')