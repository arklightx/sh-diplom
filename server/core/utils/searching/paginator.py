from rest_framework.pagination import PageNumberPagination


class Paginator(PageNumberPagination):
    page_query_param = "page"  # http://localhost:8000/.../?page=1 - по такому пути вернёт первую страницу
    max_page_size = 20  # максимум на странице может быть 20 элементов
    page_size = 15  # обычный размер страницы 15 элементов