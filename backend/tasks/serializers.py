from rest_framework import serializers

class TaskInputSerializer(serializers.Serializer):
    task_id = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=255)
    due_date = serializers.DateField(required=False)
    estimated_hours = serializers.FloatField(required=False)
    importance = serializers.IntegerField(min_value=1, max_value=10)
    dependencies = serializers.ListField(child=serializers.CharField(), required=False)
