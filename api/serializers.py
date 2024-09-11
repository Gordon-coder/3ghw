from rest_framework import serializers
from .models import Assignment

class WorkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'