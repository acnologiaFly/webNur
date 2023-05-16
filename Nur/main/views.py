from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/index.html',
                  {
                      'pr': products,
                      'category': category,
                      'categories': categories,
                  })




def product_details(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    category = Category.objects.all()

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)



    return render(request, 'main/product-detail.html', locals())

def order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    category = Category.objects.all()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            product = Product.objects.get(id=product_id)
            order_form.instance.product = product
            order_form.save()
            return redirect('/')
    else:
        order_form = OrderForm()
    context = {
        'title': 'Заказ',
        'category': category,
        'order_form': order_form,
        'product': product,
    }
    return render(request, 'main/order.html', context=context)




