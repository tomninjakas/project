from sights.migrations.serializers import UserSerializer
from sights.models import sights
from sights.serializers import sightsSerializer
import sights.serializers
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from sights.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    Returns a list of all snippets.
    """
    queryset = sights.objects.all()
    serializer_class = sightsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,]
    search_fields = ['title', 'code']
    ordering_fields = ('title', 'owner')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    class sightsDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = sights.objects.all()
        serializer_class = sightsSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

