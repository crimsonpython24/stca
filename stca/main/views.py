from django.shortcuts import render

from .models import Carousel, Notice

# Create your views here
def index(request):
    carousels = Carousel.objects.order_by('-pub_date')
    notices = Notice.objects.order_by('-pub_date')
    notice_group = [notices[i:i+3] for i in range(0, len(notices), 3)]
    context = {'carousels': carousels, 'notices': notices, 'notice_group': notice_group}
    return render(request, 'main/index.html', context)

    