from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    isCompleted = serializers.BooleanField(source='is_completed')
    isImportant = serializers.BooleanField(source='is_important')
    isDueToday = serializers.BooleanField(source='is_due_today')
    isDueTomorrow = serializers.BooleanField(source='is_due_tomorrow')
    class Meta:
        fields = (
            'id',
            'text',
            'isCompleted',
            'isImportant',
            'isDueToday',
            'isDueTomorrow',
        )
        model = Todo
