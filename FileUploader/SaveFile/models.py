from django.db import models

def upload_to_folder(instance, filename):
    ext = filename.split('.')[-1].lower()
    if ext in ['jpg', 'jpeg', 'png']:
        return f'images/{filename}'
    elif ext == 'pdf':
        return f'docs/{filename}'
    elif ext == 'zip':
        return f'zips/{filename}'
    return f'others/{filename}'

class UploadedFile(models.Model):
    file = models.FileField(upload_to=upload_to_folder)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
