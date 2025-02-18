from django.shortcuts import render
from blog.models import BlogPost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile

@login_required
def home_view(request):
    # Fetch the UserProfile instance for the current user
    queryset = BlogPost.objects.order_by('-date_posted')
    paginator = Paginator(queryset, 5)

    page = request.GET.get('page') 
    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        blog_posts = paginator.page(1)
    except EmptyPage:
        blog_posts = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'blog_posts': blog_posts})
