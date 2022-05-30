from django.db import models
from django.forms import CharField, IntegerField

# указываем поля, которые будут отобраться в постах

class Post(models.Model):
    text = models.CharField(max_length=400)
    likecount = models.IntegerField(default=0)
    date = models.DateTimeField('publish date', auto_now_add=True) 


# определим стандартное строковое определение, возвращая значение поля text
def __str__(self):
    return self.text


