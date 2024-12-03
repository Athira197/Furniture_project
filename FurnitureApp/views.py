from django.shortcuts import render,redirect
from FurnitureApp.models import FurnitureDb,ProductDb,BlogDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import ContactDb
from django.contrib import messages

def index_page(req):
    cat = FurnitureDb.objects.count()
    pro = ProductDb.objects.count()
    return render(req,"index.html",{'cat':cat,'pro':pro})
def add_cat(req):
    return render(req,"add_category.html")
def save_cat(req):
    if req.method == "POST":
        a = req.POST.get('name')
        b = req.POST.get('desc')
        c = req.FILES['image']
        obj = FurnitureDb(Category=a,Description=b,Image=c)
        obj.save()
        messages.success(req,"Category saved..!")
        return redirect(add_cat)
def display_cat(req):
    cat = FurnitureDb.objects.all()
    return render(req,"display_cat.html",{'cat':cat})
def  edit_cat(req,cat_id):
    cat = FurnitureDb.objects.get(id=cat_id)
    return render(req,"edit_cat.html",{'cat':cat})
def update_cat(req,cat_id):
    if req.method == "POST":
        a = req.POST.get('name')
        b = req.POST.get('desc')
        try:
            c = req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(c.name,c)
        except MultiValueDictKeyError:
            file=FurnitureDb.objects.get(id=cat_id).Image
        FurnitureDb.objects.filter(id=cat_id).update(Category=a,Description=b,Image=file)
        messages.success(req,"Update Succesfully...!")
        return redirect(display_cat)
def delete_cat(req,cat_id):
    x = FurnitureDb.objects.filter(id=cat_id)
    x.delete()
    messages.error(req, "Delete Succesfully...!")
    return redirect(display_cat)
def add_product(req):
    cat = FurnitureDb.objects.all()
    return render(req,"add_product.html",{'cat':cat})
def save_pro(req):
    if req.method == "POST":
        a = req.POST.get('pcat')
        b = req.POST.get('pname')
        c = req.POST.get('quantity')
        d = req.POST.get('mrp')
        e = req.POST.get('desc')
        f = req.POST.get('origin')
        g = req.POST.get('manufacture')
        h = req.FILES['img1']
        i = req.FILES['img2']
        j = req.FILES['img3']
        obj = ProductDb(Product_Category=a,Product_Name=b,Quantity=c,MRP=d,Description=e,Origin=f,Manufacture=g,Image1=h,Image2=i,Image3=j)
        obj.save()
        messages.success(req, "Product saved..!")
        return redirect(add_product)
def display_pro(req):
    pro = ProductDb.objects.all()
    return render(req,"display_product.html",{'pro':pro})
def edit_pro(req,pro_id):
    cat = FurnitureDb.objects.all()
    pro = ProductDb.objects.get(id=pro_id)
    return render(req,"edit_product.html",{'cat':cat,'pro':pro})
def update_pro(req,pro_id):
    if req.method == "POST":
        a = req.POST.get('pcat')
        b = req.POST.get('pname')
        c = req.POST.get('quantity')
        d = req.POST.get('mrp')
        e = req.POST.get('desc')
        f = req.POST.get('origin')
        g = req.POST.get('manufacture')
        try:
           h = req.FILES['img1']
           fs=FileSystemStorage()
           file=fs.save(h.name,h)
        except MultiValueDictKeyError:
            file=ProductDb.objects.get(id=pro_id).Image1
        try:
           i = req.FILES['img2']
           fs1=FileSystemStorage()
           file1=fs1.save(i.name,i)
        except MultiValueDictKeyError:
            file1=ProductDb.objects.get(id=pro_id).Image2
        try:
           j = req.FILES['img3']
           fs2=FileSystemStorage()
           file2=fs2.save(j.name,j)
        except MultiValueDictKeyError:
            file2=ProductDb.objects.get(id=pro_id).Image3
        ProductDb.objects.filter(id=pro_id).update(Product_Category=a, Product_Name=b, Quantity=c, MRP=d, Description=e, Origin=f, Manufacture=g,
                  Image1=file,Image2=file1,Image3=file2)
        messages.success(req, "Update Succesfully...!")
        return redirect(display_pro)
def delete_pro(req,p_id):
        x=ProductDb.objects.filter(id=p_id)
        x.delete()
        messages.error(req,"Deleted Successfully...!")
        return redirect(display_pro)
def login_page(req):
    return render(req,"Admin_login.html")
def admin_login(request):
    if request.method == "POST":
        a = request.POST.get('username')
        b = request.POST.get('pass')
        if User.objects.filter(username__contains=a).exists():
            user = authenticate(username=a,password=b)
            if user is not None:
                login(request,user)
                request.session['username'] = a
                request.session['password'] = b
                messages.success(request,"Welcome...!")
                return redirect(index_page)
            else:
                messages.error(request,"Please check your password..!")
                return redirect(login_page)
        else:
            messages.warning(request,"Invalid Username..!")
            return redirect(login_page)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"Logout Succesfully..!")
    return redirect(login_page)
def contact_data(request):
    info = ContactDb.objects.all()
    return render(request,"Contact_data.html",{'info':info})
def delete_contact(request, c_id):
        x = ContactDb.objects.filter(id=c_id)
        x.delete()
        return redirect(contact_data)
def add_blog(request):
    return render(request,"add_blog.html")

def save_blog(request):
    if request.method == "POST":
        a = request.POST.get('head')
        b = request.FILES['img']
        obj = BlogDb(Heading=a,BImage=b)
        obj.save()
        return redirect(add_blog)
# Create your views here.
