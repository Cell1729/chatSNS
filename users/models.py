from django.db import models

# Create your models here.

# 保存するデータ
# user名 - password

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name