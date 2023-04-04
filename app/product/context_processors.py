from product.models import *

def extras(request):
    context = {}
    context['general'] = GeneralSettings.objects.all()

    
    return context