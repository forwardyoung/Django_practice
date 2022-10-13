from django.shortcuts import render, redirect
from . forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# 인증과 관련된 곳의 forms에서 UserCreationForm을 가져온다.
# CustomUserCreationForm 반영

# Create your views here.
def index(request):
    users = get_user_model().objects.all()
    context = {
        "users" : users,
    }
    return render(request, "accounts/index.html", context)

def signup(request):
    # POST 요청 처리
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else: # 회원가입 유효성 검사 => 유효한 사용자 이름을 입력하세요. 이곳에는 문자, 숫자, @/./+/-/_만 가능합니다.
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
