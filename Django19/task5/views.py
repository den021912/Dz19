# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import UserRegister
#
# # Create your views here.
# def sign_up_by_django(request):
#     users = ['Нина', 'Миша', 'Вася', 'Света']
#     info = {}
#     len_info = len(info)
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         username1 = request.POST.get('username')
#         password1 = request.POST.get('password')
#         repeat_password1 = request.POST.get('repeat_password')
#         age1 = request.POST.get('age')
#         if form.is_valid():
#             if username1 in users:
#                 info['error'] = 'Пользователь уже существует'
#                 return render(request, 'registration_page.html', context=info)
#             elif repeat_password1 != password1:
#                 info['error'] = 'Пароли не совпадают'
#                 return render(request, 'registration_page.html', context=info)
#             elif int(age1) < 18:
#                 info['error'] = 'Вы должны быть старше 18'
#                 return render(request, 'registration_page.html', context=info)
#             else:
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
#                 repeat_password = form.cleaned_data['repeat_password']
#                 age = form.cleaned_data['age']
#                 info = {}
#                 return render(request, 'registration_page.html',
#                               context={'wellcome': f'Приветствуем, {username1}!'})
#     else:
#         form = UserRegister()
#     return render(request, 'registration_page.html')
#
#
# def sign_up_by_html(request):
#     users = ['Нина', 'Миша', 'Вася', 'Света']
#     info = {}
#     len_info = len(info)
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         username1 = request.POST.get('username')
#         password1 = request.POST.get('password')
#         repeat_password1 = request.POST.get('repeat_password')
#         age1 = request.POST.get('age')
#         if form.is_valid():
#             if username1 in users:
#                 info['error'] = 'Пользователь уже существует'
#                 return render(request, 'registration_page.html', context=info)
#             elif repeat_password1 != password1:
#                 info['error'] = 'Пароли не совпадают'
#                 return render(request, 'registration_page.html', context=info)
#             elif int(age1) < 18:
#                 info['error'] = 'Вы должны быть старше 18'
#                 return render(request, 'registration_page.html', context=info)
#             else:
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
#                 repeat_password = form.cleaned_data['repeat_password']
#                 age = form.cleaned_data['age']
#                 info = {}
#                 return render(request, 'registration_page.html',
#                               context={'wellcome': f'Приветствуем, {username1}!'})
#     else:
#         form = UserRegister()
#     return render(request, 'registration_page.html')



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