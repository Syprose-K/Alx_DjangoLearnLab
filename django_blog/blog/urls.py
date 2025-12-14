from django.urls import path, include
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    
    # CRUD for posts
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comments/new/', views.comment_create, name='comment-create'),
    path('comment/<int:pk>/edit/', views.comment_update, name='comment-update'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment-delete'),
    path('accounts/', include('django.contrib.auth.urls')),
]

#POST /post/<post_pk>/comments/new/ — create comment
#GET/POST /comment/<pk>/edit/ — edit comment (author only)
#GET/POST /comment/<pk>/delete/ — confirm & delete (author only)