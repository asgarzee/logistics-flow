from rest_framework import serializers


class FlowSerializer(serializers.Serializer):
    awb = serializers.CharField(max_length=20)
