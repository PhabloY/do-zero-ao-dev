from django.shortcuts import render


def home(requests):
    print('home')

    context = {
        'text': 'estamos na home'
    }

    return render(
        requests,
        'home/index.html',
        context,

    )
