# photos/views.py

from django.shortcuts import render, get_object_or_404
from .models import Photo
from django.db.models import Q 

def photo_list(request):
    search_query = request.GET.get('search_query', '')

    if search_query:
        photos = Photo.objects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        ).order_by('-published_at')
    else:
        photos = Photo.objects.all().order_by('-published_at')

    context = {
        'photos': photos,
        'search_query': search_query
    }
    return render(request, 'photos/photo_list.html', context)

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photos/photo_detail.html', {'photo': photo})