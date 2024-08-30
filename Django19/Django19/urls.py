from django.contrib import admin
from django.urls import path
from task1.views import class_template, games, basket, sign_up_by_django, sign_up_by_html
from task5.views import blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('yandex', class_template),
    path('yandex/games', games),
    path('yandex/basket', basket),
    path('django_sign_up/', sign_up_by_django),
    path('', sign_up_by_html),
    path('blog/', blog)
]
