from django.http import HttpResponse

def home(request):
    return HttpResponse("This is home! And here is rango: <a href='/rango/'>Rango</a>")
