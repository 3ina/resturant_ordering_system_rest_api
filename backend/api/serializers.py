from rest_framework import serializers
from backend import models


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        view_name='detail-category',
        read_only=True)

    class Meta:
        model = models.Item
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class OrderItemSerializers(serializers.ModelSerializer):
    item = serializers.HyperlinkedRelatedField(
        queryset=models.Item.objects.all(),
        view_name="detail-item",
    )

    class Meta:
        model = models.OrderItem
        fields = "__all__"


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        models = models.Payment
        fields = "__all__"

