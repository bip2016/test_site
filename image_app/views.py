from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ImgForm
from .models import Photo


# Create your views here.
def image_view(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImgForm()
    return render(request, 'upload.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def display_images(request):
    if request.method == 'GET':
        # getting all the objects.
        Photos = Photo.objects.all()
        return render(request, 'display_images.html', {'images': Photos})