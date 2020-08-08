from django.shortcuts import render
from android.models import User,Games,File,allview
from django.shortcuts import redirect
from android.forms import DocumentForm


# Create your views here.
def gamepro(request):
    Files=File.objects.all()
    return render(request,'index.html',{'Files':Files})


def searchmatch(query, item):
    if User.objects.filter(Game__icontains=query) | User.objects.filter(Username__icontains=query):
        return True
    else:
        return False


def search(request):
    query=request.GET.get('search')
    prot = User.objects.filter(Game__icontains=query) | User.objects.filter(Username__icontains=query)
    prod=[item for item in prot if searchmatch(query,item)]
    return render(request,'search.html',{'prod':prod})

def imageview(request, myid):
    prod=File.objects.filter(id= myid)
    return render(request,'image.html',{'prodd':prod})

def allimageview(request):
    allresult=allview.objects.all()
    return render(request,'allview.html',{'allresult':allresult})

def userview(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = DocumentForm()
    return render(request, 'userform.html', {
        'form': form
    })
