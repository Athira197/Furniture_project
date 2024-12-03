from django.shortcuts import render,redirect
from FurnitureApp.models import ProductDb,FurnitureDb,BlogDb
from WebApp.models import ContactDb,Registerdb,CartDb,OrderDb
from django.contrib import messages
import razorpay
def home_page(request):
    categories = FurnitureDb.objects.all()
    data = BlogDb.objects.all()
    cart_data=CartDb.objects.filter(Name=request.session['Name'])
    X=cart_data.count()
    return render(request,"Home.html",{'categories':categories,'data':data,'X':X})
def product_page(request):
    products = ProductDb.objects.all()
    categories = FurnitureDb.objects.all()
    return render(request,"Products.html",{'products':products,'categories':categories})
def about_page(request):
    categories = FurnitureDb.objects.all()
    return render(request,"About.html",{'categories':categories})
def contact_page(request):
    categories = FurnitureDb.objects.all()
    return render(request,"Contact.html",{'categories':categories})
def save_contact(request):
    if request.method == "POST":
        a = request.POST.get('fname')
        b = request.POST.get('lname')
        c = request.POST.get('ph')
        d = request.POST.get('email')
        e = request.POST.get('msg')
        obj = ContactDb(FirstName=a,LastName=b,Mobile=c,Email=d,Message=e)
        obj.save()
        return redirect(contact_page)
def filter_products(request,cat_name):
    data = ProductDb.objects.filter(Product_Category=cat_name)
    return render(request,"Products_filtered.html",{'data':data})
def single_product(request,pro_id):
    data = ProductDb.objects.get(id=pro_id)
    return render(request,"Single_Product.html",{'data':data})
def blog_page(request):
    data = BlogDb.objects.all()
    categories = FurnitureDb.objects.all()
    return render(request,"Blog.html",{'data':data,'categories':categories})
def register(request):
    return render(request,"Register.html")
def login_page(request):
    return render(request,"Login.html")
def save_register(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('ph')
        d = request.POST.get('pass')
        e = request.POST.get('re_pass')
        obj = Registerdb(Name=a,Email=b,Mobile=c,Password=d,ConformPassword=e)
        if Registerdb.objects.filter(Name=a).exists():
            messages.warning(request,"User already exists..!")
            return redirect(register)
        elif Registerdb.objects.filter(Email=b).exists():
            messages.warning(request,"Email address already exists..!")
            return redirect(register)
        obj.save()
        messages.success(request,"Registered Successfully...!")
        return redirect(register)
def user_login(request):
    if request.method == "POST":
        un = request.POST.get('your_name')
        pwd = request.POST.get('your_pass')
        if Registerdb.objects.filter(Name=un,Password=pwd).exists():
            request.session['Name'] = un
            request.session['Password'] = pwd
            messages.success(request,"Welcome..!")
            return redirect(home_page)
        else:
            messages.error(request,"Please check your password..!")
            return redirect(login_page)
    else:
        messages.warning(request,"Invalid Username..!")
        return redirect(login_page)

def user_logout(request):
    del request.session['Name']
    del request.session['Password']
    messages.success(request,"Logout Successfully..!")
    return redirect(login_page)
def save_cart(request):
    if request.method == "POST":
        a = request.POST.get('user')
        b = request.POST.get('productname')
        c = request.POST.get('quantity')
        d = request.POST.get('price')
        e = request.POST.get('total')
        try:
            Product_img = ProductDb.objects.get(Product_Name=b)
            img=Product_img.Image1
        except ProductDb.DoesNotExist:
            img=None
        obj = CartDb(Name=a,Product_Name=b,Quantity=c,Price=d,Total_price=e,Prod_Image=img)
        obj.save()
        return redirect(home_page)
def cart(request):
    data = CartDb.objects.filter(Name=request.session['Name'])
    subtotal = 0
    shipping_amount=0
    total_amount =0
    for i in data:
        subtotal=subtotal+i.Total_price
        if subtotal>50000:
            shipping_amount=100
        else:
            shipping_amount = 250
        total_amount=shipping_amount+subtotal
    return render(request,"Cart.html",{'data':data,'subtotal':subtotal,'shipping_amount':shipping_amount,'total_amount':total_amount})
def delete_cart(request,cart_id):
    x=CartDb.objects.filter(id=cart_id)
    x.delete()
    return redirect(cart)
def checkout(request):
    data = CartDb.objects.filter(Name=request.session['Name'])
    subtotal = 0
    shipping_amount = 0
    total_amount = 0
    for i in data:
        subtotal = subtotal + i.Total_price
        if subtotal > 50000:
            shipping_amount = 100
        else:
            shipping_amount = 250
        total_amount = shipping_amount + subtotal
    return render(request,"Checkout.html",{'data':data,'subtotal':subtotal,'shipping_amount':shipping_amount,'total_amount':total_amount})
def save_checkout(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mail=request.POST.get('email')
        place=request.POST.get('place')
        address=request.POST.get('address')
        phone=request.POST.get('ph')
        state=request.POST.get('state')
        pin=request.POST.get('pin')
        msg=request.POST.get('msg')
        tot=request.POST.get('total')
        obj=OrderDb(Name=name,Email=mail,Place=place,Address=address,Mobile=phone,State=state,Pin=pin,Message=msg,TotalPrice=tot)
        obj.save()
        return redirect(payment)
def payment(request):
    #retrieve the data from orderdb with the specified ID
    customer=OrderDb.objects.order_by('-id').first()
    #get the payment amount of the specified customer
    pay=customer.TotalPrice
    #covert the amount into paisa(smallest currency unit)
    amount=int(pay*100)
    pay_str=str(amount)
    for i in pay_str:
        print(i)
    if request.method=="POST":
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_b1gmX5KfBBNmX8','XxUmRDYhOuR02B6IIKsN64Cg'))
        payment=client.order.create({'amount':amount,'currency':order_currency})
    return render(request,"Payment.html",{'customer':customer,'pay_str':pay_str})
# Create your views here.
