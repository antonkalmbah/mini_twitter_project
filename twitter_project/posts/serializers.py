from rest_framework import serializers
from .models import Post


#  создаём файл, который будет преобразовывать данные для API в более простой формат. Сериализатор!
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'text', 'likeCount', 'date')