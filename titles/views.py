from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from titles.serializers import TitleSerializer
from titles.models import title


class TitleViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = title.objects.all().order_by('name')
    serializer_class = TitleSerializer  # Сериализатор для модели