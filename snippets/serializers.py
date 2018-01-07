from rest_framework import serializers
from snippets.models import (
    Snippet 
    )
from django.contrib.auth.models import User



class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'owner')
        owner = serializers.ReadOnlyField(source='owner.username')
        

# class PersonSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

#     class Meta:
#         model = Person
#         fields = ('id', 'name', 'snippets')

# class CreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Person
#         fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')