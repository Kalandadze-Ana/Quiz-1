from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def products(request):
    context = {
        'products': [
            {'name': 'Laptop', 'price': 2500},
            {'name': 'Mouse', 'price': 80},
            {'name': 'Keyboard', 'price': 150},
            {'name': 'Monitor', 'price': 700},
        ]
    }

    return render(request, "products.html", context)