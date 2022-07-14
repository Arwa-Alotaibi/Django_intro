# Create your views here.
from django.shortcuts import render, HttpResponse ,redirect



#Have the root route ("/") show a page with the form
def index(request):
    return render(request,'index.html')


def display_user(request):
    name_form=request.POST['fname']
    Dojo_location=request.POST['Dojo_location']
    Favorite_language=request.POST['Favorite-language']
    comment_form=request.POST['comment']
    context={
        'fname':name_form,
        'Dojo_location_template':Dojo_location,
        'Favorite_language':Favorite_language,
        'comment':comment_form,
    }
    
    return render(request,'show.html',context)

