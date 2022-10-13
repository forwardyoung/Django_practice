from django.contrib.auth.forms import UserCreationForm
# from .models import User
# get_user_model()은 현재 프로젝트에서 활성화된 사용자 모델을 반환

from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model = get_user_model()
		fields = ['username', 'email', 'password1', 'password2']