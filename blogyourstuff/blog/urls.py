from django.urls import path
from .views import home_view, about_view, contact_view, create_blog_post, delete_blog_post, post_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('create-post/', create_blog_post, name='create_blog_post'),
    path('delete-post/<int:post_id>/', delete_blog_post, name='delete_blog_post'),
    path('post/<int:post_id>/', post_detail_view, name='post_details'),
]
