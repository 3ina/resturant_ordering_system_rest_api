from rest_framework import generics, status
from rest_framework.response import Response

from backend.api import serializers
from backend import models
from rest_framework import permissions
from backend.api import permissions as permissionApi


# -----------------------item View---------------------
class RetrieveUpdateDeleteItem(
    generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class CreateListItemView(generics.ListCreateAPIView):
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class ListItemView(generics.ListAPIView):
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()


class RetrieveItemView(generics.RetrieveAPIView):
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()


# -----------------------category View---------------------

class RetrieveUpdateDeleteCategory(
    generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class CreateListCategoryView(generics.ListCreateAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class ListCategoryView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class RetrieveCategoryView(generics.RetrieveAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


# -----------------------order View---------------------
class CreateListOrder(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    permission_classes = [permissionApi.IsOwnerOrderOrAdmin,permissions.IsAuthenticated]
    serializer_class = serializers.OrderSerializers

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def get_queryset(self):
        user = self.request.user
        return models.Order.objects.filter(user=user)
