from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializer import NewsPortalSerializer, UserDetailsSerializer
from .models import NewsPortal
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 6


class NewsPortalViewSet(ReadOnlyModelViewSet):
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsAuthenticated,)
    queryset = NewsPortal.objects.all()
    serializer_class = NewsPortalSerializer


# class NewsPortalViewSet(APIView):
#     def get(self, request, format=None, id=None):
#         news_portal = NewsPortal.objects.all()
#         serializer = NewsPortalSerializer(news_portal, many=True)
#         return Response(serializer.data)

# class NewsPortalViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = NewsPortal.objects.all()
#         serializer = NewsPortalSerializer(queryset, many=True)
#         return Response(serializer.data)


class UserDetailsViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = get_user_model().objects.all()
    serializer_class = UserDetailsSerializer

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)