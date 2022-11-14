from titles.models import title
from rest_framework import serializers


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = title
        # Поля, которые мы сериализуем
        fields = ["pk", "name", "pg", "release", "price"]