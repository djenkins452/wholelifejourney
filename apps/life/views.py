from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def life_index(request):
    return render(request, "life/index.html")
