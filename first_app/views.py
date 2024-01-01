from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(reqeust):
    d={
        "names_string":["akash" ,"batash" ,"matash"],
        "name":'akash',
        'name':'batash',
        'age':20,
        'bari':"dhaka",
        'list':[10,20,30,40,50],
        'birthday': datetime.datetime.now(),
        'nothing':" ",
        'demo':'i am demo',
        'info':
            [
                {'name':'akash','age':20},
                {'name':'batash','age':10},
                {'name':'katash','age':15}

                ]

        }
    
    return render(reqeust,'home.html',context=d)
