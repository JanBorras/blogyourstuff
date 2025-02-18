from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost
from django.contrib.auth.decorators import login_required

@login_required
def post_detail_view(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'post_details.html', {'post': post})

