from django.contrib.auth.models import User, Group
from .models import Category, product
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'category')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category_name = serializers.ReadOnlyField()
    related = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name' )

    class Meta:
        model = product
        fields = ('id', 'name', 'description', 'image', 'category_name', 'related', )




