from rest_framework import serializers
from .models import Songs

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['id','title', 'artist', 'album', 'release_date', 'genre']