from django.shortcuts import render, redirect, get_object_or_404
from.forms import PhotoUploadForm
from.models import Photo

def photo_gallery(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'photo_gallery.html', context)

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo-gallery')
    else:
        form = PhotoUploadForm()
    return render(request, 'upload_photo.html', {'form': form})

def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.method == 'POST':
        photo.delete()
        return redirect('photo-gallery')
    context = {'photo': photo}
    return render(request, 'delete_photo_confirmation.html', context)
