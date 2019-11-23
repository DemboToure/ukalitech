from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required , user_passes_test
from .models import *
from .forms import *
# Create your views here.

@login_required(login_url='/website/login_user')
def home(request):
    folders     = ArchivingFolder.objects.filter(folder=None) 
    
    if request.method == 'POST':
        folder = ArchivingFolder()
        folder.label = request.POST['label']
        folder.save()
        
        return redirect('archivingHome')

    return render(request, 'archiving.html', locals())


@login_required(login_url='/website/login_user')
def showFolder(request, id):
    folder      = ArchivingFolder.objects.get(id=id)
    dit         = folder.getPath().split("/")
    path = []
    for d in dit:
        d = d.split("-")
        path.append({'label':d[0], 'id':d[1]})
    path.reverse()
    if request.method == 'POST':
        if 'addFolder' in request.POST:
            child = ArchivingFolder()
            child.label = request.POST['label']
            child.folder = folder
            child.save()
        elif 'addFile' in request.POST:
            fileForm = FileForm(request.POST, request.FILES)
            if fileForm.is_valid():
                fileForm.save()


        return redirect("showFolder", id)
    
    return render(request, 'folderShow.html', locals())
