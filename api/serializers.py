from .models import Illustration

from rest_framework import serializers


class IllustrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Illustration
        fields = ('title', 'description', 'image')
