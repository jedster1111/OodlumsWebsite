from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Video

def index(request):
    return HttpResponse("Hello World This is the Video app")

def detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'videos/detail.html', {'video' : video})

def list(request):
    videos = Video.objects.order_by('-pub_date')[:5]
    context = {
        'videos' : videos,
               }
    return render(request, 'videos/index.html', context)

