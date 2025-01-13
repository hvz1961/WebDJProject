from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это страница вендинговой компании КофеЛавка</h1>")
def data(request):
    return HttpResponse("<h1>Это каталог оборудования компании КофеЛавка</h1>")

def test(request):
    return HttpResponse("<h1>Это страница контактов компании КофеЛавка</h1>")
