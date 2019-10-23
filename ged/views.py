from django.shortcuts import render
from django.contrib.auth.decorators import login_required , user_passes_test

# Create your views here.

@login_required(login_url='/website/login_user')
def ged_home(request):

    return render(request, "ged.html")
