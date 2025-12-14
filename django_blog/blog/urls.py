from django.urls import path, include
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    PostByTagListView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    Path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag')

    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('search/', views.post_search, name='post-search'),
]

#POST /post/<post_pk>/comments/new/ — create comment
#GET/POST /comment/<pk>/edit/ — edit comment (author only)
#GET/POST /comment/<pk>/delete/ — confirm & delete (author only)