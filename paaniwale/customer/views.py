from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from.models import Post
# Create your views here.

def index(request):
    if request.method =='POST':
        if request.POST.get('FirstName') and request.POST.get('MiddleName') and request.POST.get('LastName') and request.POST.get('Age') and request.POST.get('Gender'):
            post = Post()
            post.FirstName = request.POST.get('FirstName')
            post.MiddleName = request.POST.get('MiddleName')
            post.LastName= request.POST.get('LastName')
            post.Age = request.POST.get('Age')
            post.Gender = request.POST.get('Gender')
            post.save()
            return render(request, 'paaniwale/base.html')
        else:
            return render(request, 'paaniwale/base.html')

    else:
        return render(request, 'paaniwale/base.html')
def details(request):
    return render(request, 'paaniwale/details.html',)

def show(request):
    DATA = Post.objects.all()
    return render(request,'paaniwale/ShowData.html',{'DATA':DATA})

