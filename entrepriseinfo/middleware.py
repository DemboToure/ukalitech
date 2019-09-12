from .models import *

def EntrepriseMiddleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print('okkk!!!!!!')
        #request.session['entrepriseinfo'] = vars(EntrepriseInfo.objects.all()[0])
        entreprise = EntrepriseInfo.objects.all()
        etr = None
        if entreprise != None:
	        etr = vars(EntrepriseInfo.objects.all()[0]) 
	        etr['img'] = etr['img'].url
	        etr.pop('_state')
	        etr.pop('_django_cleanup_original_cache')
	        request.session['entrepriseinfo'] = etr 
        #print(etr)
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware