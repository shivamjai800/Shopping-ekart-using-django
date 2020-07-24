from django.shortcuts import render
from math import ceil
from django.http import HttpResponse
from shops.models  import Product
def index(request):

    allprods=[]
    cateprods = Product.objects.values('category','id')
    # print(cateprods)
    cats = {item['category'] for item in cateprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n
        allprods.append([prod,range(1,nSlides),nSlides])
    params ={'allprods':allprods}
    
    return render(request,'shops/index.html',params)

def about(request):
    if request.method == "POST":
        print("Yes wererwerwer")
    return render(request,'shops/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request,myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,"shops/product.html",{'product':product[0]})

def checkout(request):
    return render(request,"shops/checkout.html")