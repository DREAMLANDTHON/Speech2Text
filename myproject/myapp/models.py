# models.py

from django.db import models

class Saved(models.Model):
    result = models.CharField(max_length=255)  # 예시로 CharField를 사용했습니다. 결과값의 타입에 맞게 필드를 지정하세요.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.result
