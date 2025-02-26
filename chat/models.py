from django.db import models

# Create your models here.

# 保存するデータ
# 日時 - user名 - メッセージ

class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name