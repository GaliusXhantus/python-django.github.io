from django.shortcuts import render

# Create your views here.

def IndexView(request):
    template_name = 'musicas/index.html'
    render(request, template_name) 