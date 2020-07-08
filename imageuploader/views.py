from django.shortcuts import render
from .forms import ImageForm
from django.http import HttpResponse


# Create your views here.

def index(request):

    return render(request, 'index1.html')

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, "index.html", {'form': form})

