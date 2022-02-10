from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from task_2 import serializers
from task_2 import models
from task_2 import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating users"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', 'phone',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class CourseViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating courses"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all()
    permission_classes = (permissions.UpdateOwnCourse, IsAuthenticatedOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description', 'overview', 'price', 'language', 'instructor__name', 'category__name',)

    def perform_create(self, serializer):
        """Sets the user to the logged in user"""
        serializer.save(instructor=self.request.user)

class ArticleViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating articles"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()
    permission_classes = (permissions.UpdateOwnArticle, IsAuthenticatedOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'reading_time', 'views', 'description', 'text', 'author__name',)

    def perform_create(self, serializer):
        """Sets the user to the logged in user"""
        serializer.save(author=self.request.user)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Handles retrieving the categories"""
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    """Handles retrieving the partners"""
    queryset = models.Partner.objects.all()
    serializer_class = serializers.PartnerSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
