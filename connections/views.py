from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import ConnectionInvite
from .forms import ConnectionForm

@login_required
def new_connection(request):
    if request.method == 'POST':
        connection = ConnectionInvite(from_user=request.user)
        form = ConnectionForm(data=request.POST, instance=connection)
        if form.is_valid():
            form.save()
            return redirect('account_home')
    else:
        form = ConnectionForm()
    return render(request, "connections/new_connection.html", {'form': form})

@login_required
def accept_connection(request, pk):
    connection = get_object_or_404(ConnectionInvite, pk=pk)
    if not request.user == connection.to_user:
        raise PermissionDenied
    if request.method == 'POST':
        if "accept" in request.POST:
            connect = Connection.objects.new_connection(connection)
            connection.delete()
            return redirect(connect)
        else:
            connection.delete()
            return redirect('account_home')
    else:
        return render(request, 'connections/accept_connection.html', {'connection': connection})

@csrf_exempt
def search_users(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''

    users = User.objects.filter(username__contains=search_text)

    return render(request, 'connections/ajax_search.html', {'users': users})