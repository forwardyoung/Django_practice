from django.db import models

# Create your models here.
class Todo(models.Model):
    # django에서 pk는 자동으로 만들어준다.
    content = models.CharField(max_length=80)
    """
    # default : 
    데이터를 생성할 때 값을 안 넣으면
    자동으로 값을 채워서 데이터를 생성하겠다.
    """
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateField(
        auto_now_add=True
    )  # django model 이 최초 저장(insert) 시에만 현재날짜(date.today()) 를 적용
    deadline = models.DateField(null=True)
