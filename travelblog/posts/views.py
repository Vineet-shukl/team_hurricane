from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from.models import Post


@login_required
def home_feed_view(request):
    # This view logic will only execute if the user is authenticated
    return render(request, 'home.html')


class PostCreateView(CreateView):
    #...
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    
class HomeFeedView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Return posts authored by the current user."""
        return Post.objects.filter(author=self.request.user).order_by('-created_at')