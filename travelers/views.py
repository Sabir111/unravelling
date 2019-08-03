from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def discount(request):
    return render(request,'discount.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def booking(request):
    return render(request,'booking.html')

def contact(request):
    return render(request,'contact.html')

def destination(request):
    return render(request, 'destination.html')

