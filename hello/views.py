from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello World!</h1><p>This is my Django website.</p>")
