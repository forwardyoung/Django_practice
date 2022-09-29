from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
    _todos = Todo.objects.all()
    context = {
        "todos": _todos,
    }
    return render(
        request, "todos/index.html", context
    )  # 템플릿 파일에서 변수들을 사용하기 위해 render 함수에 context를 인자로


def create(request):
    content = request.GET.get("content___")
    # 템플릿에서 데이터를 get
    # print(content) 오늘의 저녁은?이 터미널에 출력됨

    # content필드는 default 값이 정해져있지 않으므로 content값을 넣는다.
    Todo.objects.create(content=content)
    # _todos = Todo.objects.all()
    # context = {
    #     "todos": _todos,
    # }

    return render(
        request,
        "todos/index.html",
    )  # context를 create한 후 return할 때 인자로 불러와도 되긴 하나 redirect로 해보자
