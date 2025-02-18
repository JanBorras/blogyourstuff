from django.shortcuts import render, redirect
from blog.forms import BlogPostForm
from django.contrib.auth.decorators import login_required

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('home')
    else:
        # Display the form for creating a new blog post
        form = BlogPostForm()

    return render(request, 'create_blog_post.html', {'form': form})
