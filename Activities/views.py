from django.shortcuts import render

# Create your views here.


def detail(request,activity_id):

    return render(request,'activities/detail.html')

def add_act(request):
    pass
