from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseNotFound
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.template.loader import render_to_string

#views.py
from django.shortcuts import render, redirect  
from blog.forms import BlogForm  
from blog.models import BlogData  
# Create your views here.  


def addnew(request):  
    if request.method == "POST":  
        form = BlogForm(request.POST or None, request.FILES or None)  
        if form.is_valid():  
            try:  
                
                form.save()  
                return redirect('/')  
            except:  
                pass 
    else:  
        form = BlogForm()  
    return render(request,'blog/index.html',{'form':form}) 

 
def index(request):  
    bloglist = BlogData.objects.all()
    return render(request,"blog/show.html",{'bloglists':bloglist}) 

 
def edit(request, id):  
    try:
        bloglist = BlogData.objects.get(id=id)  
        return render(request,'blog/edit.html', {'bloglist':bloglist}) 
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)


 
def update(request, id):  
    bloglist = BlogData.objects.get(id=id)  
    form = BlogForm(request.POST, instance = bloglist)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'blog/edit.html', {'bloglist': bloglist})  


def destroy(request, id):  
    bloglist = BlogData.objects.get(id=id)  
    bloglist.delete()  
    return redirect("/") 

def home(request):
    return render(request, 'blog/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'blog/register.html', context)