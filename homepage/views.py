from django.shortcuts import render
from .models import age,Slider_images


# Create your views here.
def index(request):
    mod=age.objects.all()
    context={
        'mod':mod
    }
    return render(request,'index.html',context=context)

def detail(request,pk):
    mod=age.objects.get(pk=pk)
    context={
        'mod':mod
    }
    return render(request,'detail.html',context=context)

def banner(request):
    tom=Slider_images.objects.all()
    context={
        'tom':tom
    }
    return render(request,'Slider.html',context=context)
