from django.urls import path,include
from . import api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'news', api_views.NewsPortalViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    # path('news/', api_views.NewsPortalViewSet.as_view(), name='news-list'),
]