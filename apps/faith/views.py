from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def faith_index(request):
    return render(request, "faith/index.html")
