from django.http import HttpResponse

from django.shortcuts import render


def blog(requests):
    print('blog')
    return render(
        requests,
        'blog/index.html'
    )


def exemplo(requests):
    print('exemplo')
    return render(
        requests,
        'blog/exemplo.html'
    )
