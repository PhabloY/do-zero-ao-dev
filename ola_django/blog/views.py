from django.http import HttpResponse


def blog(requests):
    print('blog')
    return HttpResponse('nome do app')


def exemplo(requests):
    print('exemplo')
    return HttpResponse('exemplo')
