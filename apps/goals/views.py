from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def goals_index(request):
    return render(request, "goals/index.html")
