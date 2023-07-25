from django.shortcuts import render
from .models import Organization


def home_view(request):
    """
    Обработчик представления для домашней страницы.

    GET-запрос:
    - Извлекаем поисковый запрос из параметров запроса.
    - Используем поле full_name и short_name для полнотекстового поиска организаций, соответствующих запросу.
    - Сортируем результаты сначала по полю full_name, а затем по полю inn.

    :param request: HTTP-запрос, который содержит поисковый запрос.
    :return: Возвращает HTML-страницу 'home.html' с результатами поиска и поисковым запросом.
    """
    if request.method == 'GET':
        # Получаем поисковый запрос из параметров запроса.
        query = request.GET.get('search_query', '')

        # Используем поле full_name и short_name для полнотекстового поиска организаций, соответствующих запросу.
        results = Organization.objects.filter(full_name__icontains=query) | Organization.objects.filter(
            short_name__icontains=query)

        # Сортируем результаты сначала по полю full_name, а затем по полю inn.
        results = results.order_by('full_name', 'inn')

        # Возвращаем HTML-страницу 'home.html' с результатами поиска и поисковым запросом.
        return render(request, 'home.html', {'results': results, 'search_query': query})
