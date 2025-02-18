from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost

@login_required
def delete_blog_post(request, post_id):
    # Get the blog post object
    post = get_object_or_404(BlogPost, pk=post_id)

    # Check if the user is staff
    if not request.user.is_staff:
        # If the user is not staff, redirect them or display an error message
        return render(request, 'permission_denied.html')

    if request.method == 'POST':
        # If it's a POST request, delete the blog post
        post.delete()
        return redirect('home')  # Redirect to the home page

    # If it's not a POST request, render the confirmation template
    return render(request, 'confirm_delete.html', {'post': post})

