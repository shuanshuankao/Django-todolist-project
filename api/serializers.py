from rest_framework import serializers
from todo.models import Todo


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        field = "__all__"
