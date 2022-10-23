from django.db import models

# Create your models here.
'''
게시판 기능
- 제목(20글자 이내)
- 내용(긴 글)
- 글 작성시간/수정시간(자동으로 기록, 날짜/시간)
'''

class Article(models.Model):
    # models에 있는 Model을 상속받아서 만든다.
    title = models.CharField(max_length=20)
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 추가될 때 자동으로 기록
    updated_at = models.DateTimeField(auto_now=True) # 자동으로 기록