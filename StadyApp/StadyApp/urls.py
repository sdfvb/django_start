from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import redirect_blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blckred/', include('ckreditor_example.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('temp/', include('weather.urls')),
    path('', redirect_blog),
    path('blog/', include('blog.urls')),
    path('book/', include('book_stady.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
