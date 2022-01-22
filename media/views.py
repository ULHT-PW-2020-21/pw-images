from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Picture
from .forms import PictureForm


# Create your views here.
def index(request):
    pictures = Picture.objects.all()
    print(pictures)
    ctx = {'pictures': pictures}
    return render(request, 'media/index.html', ctx)


def upload(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('media:index'))

    form = PictureForm()
    ctx = {'form': form}
    return render(request, 'media/upload.html', ctx)


def delete(request, picture_pk):
    picture = Picture.objects.get(pk=picture_pk)
    picture.delete()
    return redirect(reverse('media:index'))


def picture(request, picture_pk):
    picture = Picture.objects.get(pk=picture_pk)
    ctx = {'picture': picture}
    return render(request, 'media/picture.html', ctx)


def edit(request, picture_pk):
    picture = Picture.objects.get(pk=picture_pk)
    form = PictureForm(request.POST or None, instance=picture)
    if form.is_valid():
        form.save()
        return redirect('media:index')

    ctx = {'form': form, 'picture': picture}
    return render(request, 'media/edit.html', ctx)

