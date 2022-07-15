# Create your views here.
from django.shortcuts import render, HttpResponse ,redirect

#Have the root route render a template that displays the number of times the client has visited this site. 
# Refresh the page several times to ensure the counter is working.
def number_visit(request):

    if 'counter' in request.session:

        request.session['counter']+= 1 
    else:


        request.session['counter']= 1

    return render(request,'index.html')


#Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.
def destroy(request):
    try:
        del request.session['counter']	
    except  KeyError:
        pass
    return redirect('/')


#NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
def add_counter(request):
    if 'counter' in request.session:
        request.session['counter']+= 2 

    
    return redirect('/')


