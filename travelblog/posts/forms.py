# posts/forms.py
from django import forms
from.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'circle']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) # Get user from view
        super().__init__(*args, **kwargs)
        if user:
            self.fields['circle'].queryset = user.joined_circles.all()