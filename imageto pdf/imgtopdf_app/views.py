from django.shortcuts import render
from PIL import Image
import os
from django.core.files.storage import default_storage
from django.conf import settings
import img2pdf

def index(request):
   if request.method=='POST':
      uploaded_file=request.FILES.get('image')
      filename = uploaded_file.name
      directory = settings.MEDIA_ROOT
      default_storage.save(f'{os.getcwd()+"/uploaded"}/{filename}', uploaded_file)

      image=Image.open(f'{os.getcwd()+"/uploaded"}/{filename}')

      pdf_bytes=img2pdf.convert(image.filename)

      file=open(f'{os.getcwd()+"/pdf"}/mypdf.pdf','wb')
      file.write(pdf_bytes)
      image.close()
      file.close()
   return render(request,'index.html')
