from django.shortcuts import render

def landing(request):

    return render(request, 'landing/landing.html', locals())

