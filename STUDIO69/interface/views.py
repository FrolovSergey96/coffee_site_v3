from django.shortcuts import render
from core.models import *


# Create your views here.
def index(request):
    context = {'products': Coffee.objects.all()}
    return render(
        request,
        'main/index.html',
        context
    )
