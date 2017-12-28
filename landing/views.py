from django.shortcuts import render

def landing(request):

    return render(request, 'landing/landing.html', locals())

def egg(request):
    a = 1
    b = 2
    suma = a+b

    return render(request, 'landing/egg.html', locals())