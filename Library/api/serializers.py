from rest_framework import serializers
from Library.models import BookInfo,Identyfires,Authors

class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'

class IdentyfiresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identyfires
        fields = '__all__'

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'