from django.shortcuts import render


def home(requests):
    print('home')
    return render(
        requests,
        'home.html'
    )
