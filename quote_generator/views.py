from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def about(request):
    return render(request, 'quote_generator/index.html')

#def about(request):
#    return render(request, 'quote_generator/about.html')
