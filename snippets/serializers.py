from rest_framework import serializers
from snippets.models import (
    Snippet,
    )
from django.contrib.auth.models import User



class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code','highlighted', 'owner')
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

# class SnippetSerializer(serializers.HyperlinkedModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

#     class Meta:
#         model = Snippet
#         fields = ('url', 'id', 'highlight', 'owner',
#                   'title', 'code', 'linenos','highlighted')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


