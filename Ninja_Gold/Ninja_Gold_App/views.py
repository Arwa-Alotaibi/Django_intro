from time import gmtime, strftime
from django.shortcuts import render
import random
from datetime import datetime
# Create your views here.
from django.shortcuts import render, HttpResponse ,redirect
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    
    if 'activities' not in request.session:
        request.session['activities']=[]

    
    return render(request,"index.html")


def porcess_money(request):
    if request.method=='POST':
        building=request.POST['building']
        if building=='Farm' or building=='Cave' or building=='House' :
            random_number = random.randint(10,20)

        else :

            random_number = random.randint(-50,50)

        request.session['gold']+=random_number
        request.session['activities'].append({
            "activityName":building,
            'value':random_number,

            "date":strftime("%m %d %Y %H : %M %p", gmtime()),

        }
        )


        return redirect('/')






        
