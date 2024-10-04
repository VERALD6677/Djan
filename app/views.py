from django.http import HttpResponse
import os
from datetime import datetime

def home_view(request):
    return HttpResponse("<h1>Список доступных страниц:</h1><ul><li><a href='/current_time/'>Текущее время</a></li><li><a href='/workdir/'>Рабочая директория</a></li></ul>")

def current_time(request):
    now = datetime.now()
    return HttpResponse(f"<h1>Текущее время: {now.strftime('%Y-%m-%d %H:%M:%S')}</h1>")

def workdir(request):
    files = os.listdir('.')
    return HttpResponse("<h1>Содержимое рабочей директории:</h1><ul>" + "".join(f"<li>{file}</li>" for file in files) + "</ul>")
