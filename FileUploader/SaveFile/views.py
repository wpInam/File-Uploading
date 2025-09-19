from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Debugging 
import sys
from pprint import pprint

def dd(var):
    pprint(var)
    sys.exit()

def index(request):
    return render(request, 'index.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']

        # store in media/ folder
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)

        return render(request, 'index.html', {'file_url': file_url})

    return render(request, 'index.html')
