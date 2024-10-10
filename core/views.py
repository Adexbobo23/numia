from django.shortcuts import render
from .models import Team, Product

def home(request):
    team = Team.objects.all()
    product = Product.objects.all()

    context = {
        'staff': team,
        'product': product
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def booking(request):
    return render(request, 'booking.html')


def contact(request):
    return render(request, 'contact.html')


def menu(request):
    return render(request, 'menu.html')


def service(request):
    return render(request, 'service.html')


def team(request):
    return render(request, 'team.html')


def testimonial(request):
    return render(request, 'testimonial.html')