from django.shortcuts import render, redirect
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

    # context를 create한 후 return할 때 인자로 불러와도 되긴 하나 redirect로 해보자
    return redirect("todos:index")  # runserver하면 루트 주소로 뜬다.
    # 주소창에 naver를 navet로 입력해도 naver로 연결하는 역할


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect("todos:index")

    """
    redirect
    1. 사용자가 create 요청
    2. 서버에서 index 요청
    3. 사용자에게는 index 응답
    """
