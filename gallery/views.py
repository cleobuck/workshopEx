from django.views import generic
from django.urls import reverse_lazy 
from .forms import PostForm 
from .models import Post
# Create your views here.

class index(generic.ListView):
    model = Post
    template_name="pages/index.html"

class CreatePostView(generic.CreateView): 
    model = Post
    form_class = PostForm
    template_name = 'pages/post.html'
    success_url = reverse_lazy('gallery:index')