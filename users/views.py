from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def users(request):
    return render(request, 'users/index.html')
