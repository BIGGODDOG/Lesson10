from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404

# Используя механизм маршрутизации создайте
# веб-приложение, отображающее разные разделы с информацией о компании. В приложении должны быть
# такие разделы:
# ■ Главная;
# ■ Новости;
# ■ Руководство компании;
# ■ О компании;
# ■ Контакты.

# Create your views here.
def main(request: HttpRequest) -> HttpResponse:
    return render(request, "main.html")

def news(request: HttpRequest) -> HttpResponse:
    return render(request, "news.html")

def management(request: HttpRequest) -> HttpResponse:
    return render(request, "management.html")

def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")

def contacts(request: HttpRequest) -> HttpResponse:
    return render(request, "contacts.html")

def branches(request: HttpRequest) -> HttpResponse:
    return render(request, "branches.html")

def get_branch(request: HttpRequest, city_name: str) -> HttpResponse:
    # Берём данные из БД
    # city = get_object_or_404(Cities, name=city_name)
    
    return render(request, "get_branch.html", {"city_name": city_name})