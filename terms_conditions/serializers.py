from rest_framework import serializers
from .models import term_cond

class TermsconSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = term_cond
        fields = ['id', 'url', 'cond']