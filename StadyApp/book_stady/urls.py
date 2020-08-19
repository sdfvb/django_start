from django.urls import path
from .views import *


urlpatterns = [
    path('', BookPageView.as_view(), name='book_page'),
]
