from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def portfolio(request):
    return render(request, 'blog/portfolio.html')

def services(request):
    return render(request, 'blog/services.html')

def contact(request):
    return render(request, 'blog/contact.html')