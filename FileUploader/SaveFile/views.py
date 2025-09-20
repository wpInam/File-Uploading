from django.shortcuts import render
from .models import UploadedFile

def index(request):
    files = UploadedFile.objects.all().order_by('-uploaded_at')
    return render(request, 'index.html', {'files': files})

def upload_file(request):
    # Upload files: Go to UploadedFile and save the data at their
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = UploadedFile(file=request.FILES['file'])
        uploaded_file.save()  # saves file & DB record
        files = UploadedFile.objects.all().order_by('-uploaded_at')
        return render(request, 'index.html', {'files': files})

    files = UploadedFile.objects.all().order_by('-uploaded_at')
    return render(request, 'index.html', {'files': files})
