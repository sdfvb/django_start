from django.urls import path, include

from .views import PostView, PostDetail

urlpatterns = [

    path('', PostView.as_view(), name='post_view_ckeditor'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_ckeditor'),
]
