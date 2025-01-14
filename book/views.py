from django.shortcuts import render, redirect
# relative import of forms
from .models import *
from .forms import *

def landing(request, category=None):
    context ={}
    if category == None:
        
        context["products"] = Products.objects.all()
        context["categories"] = Categories.objects.all()
        print(print(context["categories"]))

        return render(request, "index.html", context)
    else:
        print(category)
        context["products"] = Products.objects.filter(category_id = category)
        print(context["products"])
        context["categories"] = Categories.objects.all()
        print(print(context["categories"]))
        return render(request, "index.html", context)
    
def detail_view(request, id):
    context ={}

    context["reviews"] = Reviews.objects.filter(product_id = id)
    context["product"] = Products.objects.get(id = id)
    related_category = context["product"].category_id
    # print(related_category)
    context["related_products"] = Products.objects.filter(category_id=related_category).exclude(id=id)
    context["categories"] = Categories.objects.all()
    return render(request, "product.html", context)

def review_view(request):
    if request.method == "POST":
        form = ReviewsForm(request.POST)
        
        if form.is_valid():
            form.save()
            id = request.POST.get('product_id')
            return redirect('detail', id=id)