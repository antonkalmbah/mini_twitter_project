from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Post
from .serializers import *

@api_view(['GET', 'POST'])
def posts(request):
    # здесь получаем ифно о том, что мы получили GET-запрос
    if request.method == 'GET':
        # получаем все модели из Post из папки .models
        posts = Post.objects.all()
        # отправляем их в сериалайзер
        serializer = PostSerializer(posts, many = True)
        # возвращаем объект
        return(Response({'data': serializer.data}))
    # если мы отправляем данные на сервер в виде POST-запроса, то нам нужен только текст, который мы получаем, 
    # сохраняем и получаем статус, что всё ок
    elif request.method == 'POST':
        post = Post()
        post.text = request.data['text']
        post.save()
        return Response(status=status.HTTP_200_OK)

# создаём функция для лайков
@api_view(['GET'])
def like_post(request, post_id):
    # получаем 1 пост соответственно по id, либо возвращаем ошибку
    if request.method == 'GET':
        try:
            post = Post.objects.get(id = post_id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # добавляем 1 лайк и сохраняем. Возвращаем статус, что всё ок
    setattr(post, 'likeCount', post.likeCount + 1)
    post.save()
    return Response(status=status.HTTP_200_OK)