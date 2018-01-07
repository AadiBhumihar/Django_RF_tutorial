from rest_framework import serializers
from snippets.models import (
    Snippet ,
    Person,)
from django.contrib.auth.models import User



class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'person')
        owner = serializers.ReadOnlyField(source='owner.username')
        

class PersonSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = Person
        fields = ('id', 'name', 'snippets')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = Person
        fields = ('id', 'username', 'snippets')