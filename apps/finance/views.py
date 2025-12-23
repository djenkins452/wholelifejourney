from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def finance_index(request):
    return render(request, "finance/index.html")
