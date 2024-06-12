from rest_framework import serializers
from sights.models import sights, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class sightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = sights
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


class UserSerializer(sights.ModelSerializer):
    sights = serializers.PrimaryKeyRelatedField(many=True, queryset=sights.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'sights']
