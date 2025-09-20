from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os

def index(request):
    return render(request, 'index.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        ext = os.path.splitext(file.name)[1].lower()

        # Decide folder based on extension
        if ext in ['.jpg', '.jpeg', '.png']:
            folder = "images"
        elif ext == '.pdf':
            folder = "docs"
        elif ext == '.zip':
            folder = "zips"
        else:
            return render(request, 'index.html', {
                'error': "Invalid file type! Only images, PDFs, and ZIPs allowed."
            })

        # Save in correct folder inside MEDIA_ROOT
        fs = FileSystemStorage(location=os.path.join("media", folder), base_url=f"/media/{folder}/")
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)

        return render(request, 'index.html', {'file_url': file_url})

    return render(request, 'index.html')
