from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Products

def home(request):
    return render(request,'cdlogin.html')

def userlogin(request):
    userid=request.POST.get('userid')
    password=request.POST.get('password')
    if userid=="tharun" and password=="123":
        return render(request,'cdproducts.html')
    else:
        return HttpResponse("details are mismatched")


def add_products(request):
    if Products.objects.count() == 0: 
        Products.objects.create(name="AVM", detail="Real-time bus health tracking system.", learning_percentage=0)
        Products.objects.create(name="Bustime", detail="shares the information regarding bus arrival depature time", learning_percentage=0)
        Products.objects.create(name="Clevercad", detail="System for managing bus operations in real-time.", learning_percentage=10)
        Products.objects.create(name="Cleverreports", detail="Reporting tool for analyzing transit data.", learning_percentage=20)
        Products.objects.create(name="Cleverworks", detail="Solution for managing maintenance and operations.", learning_percentage=15)
        
        return HttpResponse("Products added successfully!")
    else:
        return HttpResponse("Products already exist in the database.")
    
def getdetails(request):
    products=Products.objects.all()
    return render(request,'show.html',{'products':products})

def select_products(request):
     selected_product=None
     selected_product=request.POST.get('product_name')
     products=Products.objects.all()
     for i in products:
         if i.name.lower()==selected_product:
            alldetails={
                'product_name':i.name,
                'product_detail':i.detail,
                'product_percentage':i.learning_percentage
                 
             }
            return render(request,'cdproducts.html',alldetails)
def update_product(request):
    product_name=request.POST.get('product_name')
    product=Products.objects.get(name=product_name)
    context={
        'product_name':product_name,
        'product_detail':product.detail,
        'product_percentage':product.learning_percentage
    }

    return render(request,'cdupdate.html',context)

def update_details(request):
    product_name=request.POST.get('product_name')
    product_percentage=request.POST.get('product_percentage')
    product_detail=request.POST.get('product_detail')
    product=Products.objects.get(name=product_name)
    product.learning_percentage=int(product_percentage)
    product.detail=product_detail
    product.save()
    return render(request,'cdproducts.html')

def productpage(request):
    return render(request,'cdproducts.html')

def loginpage(request):
    return render(request,'cdlogin.html')



     
   


