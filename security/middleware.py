from .models import *
from django.shortcuts import render, redirect

#import django.http.request

def SecurityMiddleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        pth = request.path.split("/")
        app = Application.objects.all() 
        print(app)

        for ap in app:
            if ap.name in pth:
                if not ap.isAuthorized(request.user.id):
                    return redirect("home")

        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print('okkk!!!!!!')
        # request.session['entrepriseinfo'] = vars(EntrepriseInfo.objects.all()[0])
        

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware