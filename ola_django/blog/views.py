from django.http import HttpResponse


def blog(requests):
    print('blog')
    return HttpResponse('blog')
