# Create your views here.
from turtle import title
from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse

#/ - redirects to the "/blogs" route with a method called "root"
def root(request):
    return redirect("/blogs")


#/blogs - display the string "placeholder to later display a list of all blogs" with a method named "index"
def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')


#/blogs/new - display the string "placeholder to display a new form to create a new blog" with a method named "new"

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

#/blogs/create - redirect to the "/" route with a method called "create"
def create(request):

    return redirect('/')

#/blogs/< number > - display the string "placeholder to display blog number: {number}" with a method named "show" 
# (eg. localhost:8000/blogs/15 should display the message: 'placeholder to display blog number 15')

def show(request,number):
    return HttpResponse(f'placeholder to display blog number: {number}')


#/blogs/< number >/edit - display the string "placeholder to edit blog {number}" with a method named "edit"

def edit(request,number):
    return HttpResponse(f'placeholder to edit blog:{number}')


#/blogs/< number >/delete - redirect to the "/blogs" route with a method called "destroy"

def destroy(request,number):
    return redirect('/blogs')


#(**Bonus**) /blogs/json - return a JsonResponse with title and content keys.

def Json_Response(request):
    return JsonResponse({'title':'My First blog', 'content':'lorem,ipsum dolor sit amet consecteur adipisicing elit.' })
