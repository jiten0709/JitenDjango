from django.shortcuts import render

# Create your views here.
def home_app(request):
    return render(request, 'practiceApp/home_app.html')