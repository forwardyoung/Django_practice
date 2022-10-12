from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# 인증과 관련된 곳의 forms에서 UserCreationForm을 가져온다.

# Create your views here.
def signup(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
