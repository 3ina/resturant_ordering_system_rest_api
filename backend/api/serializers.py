from rest_framework import serializers
from backend import models


class ItemSerializer(serializers.models):
    class Meta:
        model = models.Item
        fields = "__all__"


class CommentSerializer(serializers.models):
    class Meta:
        model = models.Comment
        fields = "__all__"
