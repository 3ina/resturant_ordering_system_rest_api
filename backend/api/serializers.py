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

