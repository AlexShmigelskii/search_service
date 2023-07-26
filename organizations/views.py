from django.shortcuts import render
from django.contrib.postgres.search import SearchVector, SearchRank
from django.db.models import F
from .models import Organization


def home_view(request):
    """
    Обработчик представления для домашней страницы.

    GET-запрос:
    - Извлекаем поисковый запрос из параметров запроса.
    - Используем SearchVector для выполнения полнотекстового поиска по полям full_name и short_name.
    - Используем SearchRank для определения релевантности результатов поиска.
    - Сортируем результаты по убыванию релевантности (ранку полнотекстового поиска) и по полному наименованию.

    :param request: HTTP-запрос, который содержит поисковый запрос.
    :return: Возвращает HTML-страницу 'home.html' с результатами поиска и поисковым запросом.
    """
    if request.method == 'GET':
        # Получаем поисковый запрос из параметров запроса.
        query = request.GET.get('search_query', '')

        # Используем SearchVector для выполнения полнотекстового поиска по полям full_name и short_name.
        vector = SearchVector('full_name', 'short_name')
        results = Organization.objects.annotate(search=vector).filter(search=query)

        # Используем SearchRank для определения релевантности результатов поиска.
        rank = SearchRank(vector, query)
        results = results.annotate(rank=rank)

        # Сортируем результаты по убыванию релевантности (ранку полнотекстового поиска) и по полному наименованию.
        results = results.order_by('-rank', F('full_name'))

        # Возвращаем HTML-страницу 'home.html' с результатами поиска и поисковым запросом.
        return render(request, 'home.html', {'results': results, 'search_query': query})
