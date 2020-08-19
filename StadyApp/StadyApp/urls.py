from django.contrib import admin
from django.urls import path, include

from .views import redirect_blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('temp/', include('weather.urls')),
    path('', redirect_blog),
    path('blog/', include('blog.urls')),
    path('book/', include('book_stady.urls')),
]
