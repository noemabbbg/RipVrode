from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from titles.serializers import TitleSerializer
from titles.models import title, range, genre
from datetime import date



class TitleViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = title.objects.all().order_by('name')
    serializer_class = TitleSerializer  # Сериализатор для модели






def start(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['качество', 'комфорт', 'эмоции']
    }})


def GetMain(request):
    return render(request, 'main.html', {'data':{
        'current_date': date.today(),
        'test': range.objects.all()}})

def GetGenres(request):
	return render(request, 'genres.html', {'data':{
		'genres':genre.objects.all()
	}})

def GetTitles(request, id):
	return render(request, 'title.html', {'data':{
		'genre':genre.objects.filter(id=id)[0],
		'title': title.objects.filter(genre_id=id).all(),
        'idfor' : id
	}})













def GetCatalog(request):
    return render(request, 'catalog.html')


def GetManga(request):
    return render(request, 'manga.html')

def GetMarvel(request):
    return render(request, 'marvel.html')
