from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.views.generic import ListView

# Create your views here.
def post_list(request):
    posts = Post.published.all()  # Retrieve all published posts
    # Pagination with 3 posts per page
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        #If page_number is not an integer get the first page
        posts = paginator.page(1)    
    except EmptyPage:
        # If page_number is out the range get last page of results
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year = year,
        publish__month = month,
        publish__day=day
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )

class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'