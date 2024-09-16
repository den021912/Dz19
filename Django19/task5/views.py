from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.

def blog(request):
    per_pages = [1, 3, 5, 7, 10, ]
    posts = Post.objects.all().order_by('-created_at')
    if request.GET.get('per_page') is not None:
        per = request.GET.get('per_page')
        per_pages[0] = per
        paginator = Paginator(posts, per)
    else:
        per = per_pages[0]
        paginator = Paginator(posts, per)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'per_pages': per_pages,
        'per': per,
        'post_list': posts,
        'current_per_page': per,
    }
    return render(request, 'post_page.html', context=context)
