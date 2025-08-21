from django.contrib import admin
from django.urls import path, include
from posts.views import HomeFeedView # Assuming home feed is in posts app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('', HomeFeedView.as_view(), name='home'),
    path('', include('circles.urls')),
    path('circles/', include('circles.urls', namespace='circles')),
    path('posts/', include('posts.urls', namespace='posts')),
]