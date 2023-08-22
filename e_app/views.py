from django.shortcuts import render

def home_view(request):
    return render(request, 'e_app/e_app.html')

def about_view(request):
    return render(request, 'e_app/about.html')
