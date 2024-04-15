from rest_framework import serializers

from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(source="creator.email", read_only=True)

    class Meta:
        model = Todo
        fields = "__all__"

    def create(self, validated_data):
        creator = self.context["request"].user
        validated_data["creator"] = creator
        return super().create(validated_data)
