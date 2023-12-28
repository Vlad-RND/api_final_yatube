from django.urls import include, path
from rest_framework import routers

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router_ver_1 = routers.DefaultRouter()

router_ver_1.register(r'follow', FollowViewSet, basename='follow')
router_ver_1.register(r'groups', GroupViewSet, basename='groups')
router_ver_1.register(r'posts', PostViewSet, basename='posts')
router_ver_1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)


urlpatterns = [
    path('v1/', include(router_ver_1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
