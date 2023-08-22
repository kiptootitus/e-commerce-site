from django.shortcuts import render

def home_view(request):
    return render(request, 'e_app/e_app.html')

# Or a similar one-liner version using lambda
# home_view = lambda request: render(request, 'e_app/e_app.html')
