from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializer import NewsPortalSerializer
from .models import NewsPortal
from rest_framework.response import Response
from django.http import JsonResponse

class NewsPortalViewSet(ReadOnlyModelViewSet):
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
