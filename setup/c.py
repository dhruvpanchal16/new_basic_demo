from django.http import HttpResponse

def home(request):
    html = """
    <h1>Simple Calculator</h1>
    <a href='/add'>Addition</a><br>
    <a href='/sub'>Subtraction</a><br>
    <a href='/mul'>Multiplication</a><br>
    <a href='/div'>Division</a>
    """
    return HttpResponse(html)

def add(request):
    return HttpResponse("10 + 5 = 15")

def sub(request):
    return HttpResponse("10 - 5 = 5")

def mul(request):
    return HttpResponse("10 * 5 = 50")

def div(request):
    return HttpResponse("10 / 5 = 2")