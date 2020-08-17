from django.contrib import admin
from django.urls import path, include

from .views import redirect_blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('temp', include('weather.urls')),
    path('', redirect_blog),
    path('blog/', include('blog.urls')),
]
