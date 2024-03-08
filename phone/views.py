from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.template import loader
from .models import Items,ItemDetails,Cart,DeviceDetails,Device
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateUserForm,LoginUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate



# Create your views here.

def index(request):
    template=loader.get_template('index.html')
    context={
        
         'request':request
    }
    return HttpResponse(template.render(context))

def payment(request):
    template=loader.get_template('payment.html')
    Device=DeviceDetails.objects.select_related('itemsid')
    context={
        'request':request,
        'Device':Device
    }
    return HttpResponse(template.render(context))


def showphone(request):
    template=loader.get_template('showphone.html')
    phone=ItemDetails.objects.select_related('itemsid')

    print(phone.query)
    context={
         'request':request,'phone':phone
    }
    return HttpResponse(template.render(context))

def showdevice(request):
    template=loader.get_template('showdevice.html')
    Device=DeviceDetails.objects.select_related('itemsid')

    print(Device.query)
    context={
         'request':request,'Device':Device
    }
    return HttpResponse(template.render(context))




def Device(request,id):
    template=loader.get_template('Device.html')
    currentuser=request.user
    print(currentuser.id)
    Device=DeviceDetails.objects.select_related('itemsid').filter(id=id)
    print(Device.query)
    context={
        'Device':Device,
         'request':request
    }
    return HttpResponse(template.render(context))


def details(request,id):
    template=loader.get_template('details.html')
    currentuser=request.user
    print(currentuser.id)
    phone=ItemDetails.objects.select_related('itemsid').filter(id=id)
    print(phone.query)
    context={
        'phone':phone,
        'request':request
    }
    return HttpResponse(template.render(context))


# @csrf_exempt
# def auth_login(request):
#     form=LoginUserForm()
#     if request.method =="POST":
#         form=LoginUserForm(data=request.POST)
#         if form.is_valid():
#             username=form.changed_data['username']
#             password=form.changed_data['password']

#             user=authenticate(username=username,password=password)
#             if user :
#                 if user.active:
#                     login(request,user)
#                     return render(request,'index.html')
#     context={"form":form}
#     return render(request,'auth_login.html',context)

@csrf_exempt
def auth_login(request):
    
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = LoginUserForm(request)
    context = {
        "form": form
    }
    return render(request, "auth_login.html", context)


# @csrf_exempt
# def auth_register(request):
#     template=loader.get_template('auth_register.html')
#     form=CreateUserForm()
#     if request.method =='POST':
#         form=CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('auth_login')
#     context={'registerform':form}
#     return HttpResponse(template.render(context=context))
@csrf_exempt
def auth_register(request):
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        user_obj=form.save()
        return redirect('/auth_login')
    context = {"form": form}
    return render(request, "auth_register.html", context)

@csrf_exempt
@login_required(login_url='/auth_login/')
def checkout(request):
    template=loader.get_template('checkout.html')
    current_user=request.user.id
    cart=Cart.objects.all().filter(Id_user=current_user).first()
    prodcut=Items.objects.get(id=cart.id)
    print(cart)
    context={
        'request':request,
        'cart':cart,
        'prodcutname':prodcut,
    }
    return HttpResponse(template.render(context=context))

@csrf_exempt
def auth_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("/showphone")
    return render(request, "auth_logout.html", {})


def add_to_cart(request,id):
    currentuser=request.user
    discount=2
    state=False
    phone=ItemDetails.objects.select_related('itemsid').filter(id=id)
    for item in phone:
        net=item.total-discount
    cart = Cart(
    Id_user=currentuser.id,
    Id_proudct=item.id,
    price=item.price,
    qty=item.qty,
    tax=item.tax,
    total=item.total,
    discount=discount,
    net=net,
    status=state
    )
    cart.save()
    return redirect('/')
pass

def add_to_Cart(request,id):
    currentuser=request.user
    discount=2
    state=False
    Device=ItemDetails.objects.select_related('itemsid').filter(id=id)
    count=0
    for item in Device:
        net=item.total-discount
        count=count+1
    cart = Cart(
    Id_user=currentuser.id,
    Id_proudct=item.id,
    price=item.price,
    qty=item.qty,
    tax=item.tax,
    total=item.total,
    discount=discount,
    net=net,
    status=state
    )
    currentuser=request.user.id
    count=Cart.objects.filter(Id_user=currentuser).count()
    print(count)
    cart.save()
    request.session['countcart']=count
    return redirect('/showdevice')


