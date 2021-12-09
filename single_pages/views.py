from django.shortcuts import render

# Create your views here.
def big_moon(request):
    return render(
        request,
        'single_pages/big_moon.html'
    )