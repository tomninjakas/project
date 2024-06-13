from sights.migrations.serializers import UserSerializer
from sights.models import sights
from sights.permissions import IsOwnerOrReadOnly
from sights.serializers import SightsSerializer
import sights.serializers
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
import sights.permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SightsList(generics.ListCreateAPIView):
    """
    Returns a list of all snippets.
    """
    queryset = sights.objects.all()
    serializer_class = SightsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,]
    search_fields = ['title', 'code']
    ordering_fields = ('title', 'owner')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    class SightsDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = sights.objects.all()
        serializer_class = SightsSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
