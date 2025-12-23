from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def learning_index(request):
    return render(request, "learning/index.html")
