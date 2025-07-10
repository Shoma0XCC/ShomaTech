from django.shortcuts import render

def main(request):
    return render(request, 'page/main.html')


def about(request):
    return render(request, 'page/about.html')

def service(request):
    return render(request, 'page/service.html')


def solution(request):
    return render(request, 'page/solutions.html')

def contact(request):
    return render(request, 'page/contact.html')

def system_112(request):
    return render(request, 'page/112.html')

def error_404_view(request):
    return render(request, 'page/404.html', status=404)