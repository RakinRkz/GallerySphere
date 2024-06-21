from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('photos/', include('photos.urls')),
    path('', views.photo_gallery, name='photo-gallery'),
    path('upload/', views.upload_photo, name='upload-photo'),
    path('delete/<int:photo_id>/', views.delete_photo, name='delete-photo'),
]
