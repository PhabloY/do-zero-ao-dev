from django.shortcuts import render


def home(requests):
    print('home')

    context = {
        'text': 'Home'
    }

    return render(
        requests,
        'home/index.html',
        context,

    )
