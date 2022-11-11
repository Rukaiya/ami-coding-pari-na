from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from khoj_app.models import Khoj


class KhojSerializer(ModelSerializer):
    timestamp = serializers.CharField(source='created_at')
    input_values = serializers.CharField(source='input_value')

    class Meta:
        model = Khoj
        fields = [ 'timestamp', 'input_values']