from rest_framework import serializers

from .models import List


class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ('keyword', 'remainderTime', 'details')
