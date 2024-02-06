from rest_framework import generics
from backend.api import serializers
from backend import models
from rest_framework import permissions


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


# -----------------------comment View---------------------

