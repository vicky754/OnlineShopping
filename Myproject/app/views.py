from django.shortcuts import render,HttpResponse,redirect
from app.models import product,ProductImages
from app.authforms import CustomerCreationForm, UserCreationForm, CustomerAuthForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.views import View
# Create your views here.

def home(request):
    products=product.objects.filter(active=True)
    data={
        'products':products
    }
    return render(request,"home.html",data)

#using form view
'''class loginview(View):
    form_class=AuthenticationForm
    template_name='loginPage.html'
    success_url='/'

    def form_valid(self,form):
        #username = form.cleaned_data.get('username')
        #password = form.cleaned_data.get('password')
        #user= authenticate(username=username,password=password)
        #print(user)
        #return HttpResponse(user.username)
        #login(self.request,user)
        print(self.request)
        return super().form_valid(form)
'''

'''
#class base view
class loginview(View):
    def get(self,request):
        form = AuthenticationForm()
        context={
            'form':form
        }
        return render(request,"loginPage.html",context=context)


    def post(self,request):
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            #print(user)
            #return HttpResponse(user.username)
            login(request,user)
            return redirect('home')   
        else:
            context={
                'form':form
            }
            return render(request,"loginPage.html",context=context)
'''

#function based view
def loginview(request):
    if request.method =="GET":
        form = CustomerAuthForm()
        context={
            'form':form
        }
        return render(request,"loginPage.html",context=context)

    if request.method == "POST":
        form = CustomerAuthForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            #print(user)
            #return HttpResponse(user.username)
            login(request,user)
            return redirect('home')   
        else:
            context={
                'form':form
            }
            return render(request,"loginPage.html",context=context)


def productDetails(request,product_id):
    products=product.objects.get(id=product_id)
    images=ProductImages.objects.filter(product=product_id)
    return render(request,"product_detail.html",{'products':products, 'images':images}) 


def signup(request):
    if request.method == 'GET':
        form = CustomerCreationForm()
        context= {
            'form':form
        }
        return render(request,'signup.html',context=context)
    else:
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.email = user.usrname
            user.save()
            return render(request,'loginPage.html')
    context= {
        'form':form
        }
    return render(request,'signup.html',context=context)

    # if request.method == 'POST':
    #     form =UserCreationForm(request.POST)
    #     context= {
    #         'form':form
    #     }
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
            
def signout(request):
    logout(request)
    #request.session.clear()
    return redirect(home)

