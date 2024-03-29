from rest_framework import generics
from django.contrib.auth.models import User
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


# -----------------------order View---------------------
class CreateListOrder(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.OrderSerializers

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def get_queryset(self):
        user = self.request.user
        return models.Order.objects.filter(user=user)


class OrderDetail(generics.RetrieveAPIView):
    queryset = models.Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.OrderSerializers
    def get_queryset(self):
        user = self.request.user
        return models.Order.objects.filter(user=user)

class ListAllOrders(generics.ListAPIView):
    queryset = models.Order.objects.all()
    permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]
    serializer_class = serializers.OrderSerializers

class RetrieveUserOrder(generics.ListAPIView):
    queryset = models.Order.objects.all()
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]
    serializer_class = [serializers.OrderSerializers]

    def get_queryset(self):
        user_id = self.kwargs.get("pk")
        user = User.objects.get(pk=user_id)
        return models.Order.objects.filter(user=user)
# -----------------------orderItem View---------------------

class CreateOrderItem(generics.ListCreateAPIView):
    queryset = models.OrderItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.OrderItemSerializers


    def perform_create(self, serializer):
        user = self.request.user
        order_pk = self.kwargs.get("pk")
        try:
            order = models.Order.objects.get(pk=order_pk,user=user)
        except:
            raise Exception("order not found")
        serializer.save(user=user,order=order)

    def get_queryset(self):
        user = self.request.user
        return models.OrderItem.objects.filter(user=user,order__user=user)

# -----------------------Payment View---------------------

class CreatePayment(generics.ListCreateAPIView):
    queryset = models.Payment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.PaymentSerializers

    def perform_create(self, serializer):
        user = self.request.user
        order_pk = self.kwargs.get("pk")
        try:
            order = models.Order.objects.get(pk=order_pk,user=user)
        except:
            raise Exception("order not found")
        serializer.save(user=user,order=order)


class ListPayment(generics.ListAPIView):
    queryset = models.Payment.objects.all().order_by("paymentDate")
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.PaymentSerializers
