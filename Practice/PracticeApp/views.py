from django.shortcuts import render, get_object_or_404
from .models import Menu, Store
from .forms import MenuForm

# Create your views here.
def home_app(request):
    return render(request, 'practiceApp/home_app.html')

def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'practiceApp/menu.html', {'menu_items': menu_items})

def item_detail(request, item_id):
    item = get_object_or_404(Menu, pk=item_id)
    return render(request, 'practiceApp/item_detail.html', {'item': item})

def menu_items_view(request):
    stores = None
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu_items = form.cleaned_data['menu_items']
            stores = Store.objects.filter(item_varieties=menu_items)
    else:
        form = MenuForm()

    return render(request, 'practiceApp/menu_items_view.html', {'form': form, 'stores': stores})
