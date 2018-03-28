from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate,login,logout,get_user_model
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
import pandas as pd
from django.http import HttpResponse

def index(request):
    render(request,'power/index.html')


def signupview(request):
    if request.method == 'POST':
        form = SignuForm(request.POST)

        if(form.is_valid()):
            user = form.save()
            user.refresh_from_db()
            user.userinfo.mobile_number = form.cleaned_data.get('mobile_number')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = user.username, password= raw_password)
            login(request,user)
            return render(request,'power/logged_in.html')

    else:
        form = SignuForm()
    return render(request,'power/signup.html',{'form':form})

def logged_in(request):
    return render(request, 'power/logged_in.html')

def graph(request):
    fig = Figure()
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("~/SIH2018/MOP7/ghi2017.csv")
    data_df.values.tolist()
    print(data_df)
    return render(request,'power/logged_in.html')

def slider(request):

    #return render(request,'power/logged_in.html')
# Create your views here.
