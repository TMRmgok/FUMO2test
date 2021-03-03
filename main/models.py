from django.db import models

class Task(models.Model):
    v1 = models.CharField('Вопрос', max_length=255)
    v2 = models.CharField('Ответ 1', max_length=255)
    v3 = models.CharField('Ответ 2', max_length=255)
    v4 = models.CharField('Ответ 3', max_length=255)
    v5 = models.CharField('Ответ 4', max_length=255)
    v6 = models.CharField('Прав ответ', max_length=255)

    def __str__(self):
        return self.v1
# Create your models here.

class Globvar(models.Model):
    prO = models.CharField('Правильный ответ', max_length=255)


    def __str__(self):
        return self.v1