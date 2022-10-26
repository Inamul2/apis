from rest_framework import serializers
from .models import CustomerData


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerData
        fields = '__all__'
