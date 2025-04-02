from django.http import HttpResponse


def home(requests):
    print('home')
    return HttpResponse('home1')
