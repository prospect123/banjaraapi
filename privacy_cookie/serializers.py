from rest_framework import serializers
from .models import cookies

class CookieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cookies
        fields = ['id', 'url', 'name']