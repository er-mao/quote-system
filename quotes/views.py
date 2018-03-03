from django.shortcuts import render

# Create your views here.


def quotes(request):
    return render(request, 'quotes.html')
