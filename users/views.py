from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from database.models import Orders, Quotes

# Create your views here.


@login_required
def users(request):
    username = request.user.get_username()
    return render(request,
                  'users/index.html',
                  {'username': username,
                   'orders_table': Orders.objects.all(),
                   'quotes_table': Quotes.objects.select_related('requirement').all()})
