from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, Django!")
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

def menu(request):
    return render(request, 'practiceApp/menu.html')
