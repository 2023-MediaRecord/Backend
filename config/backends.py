# your_app/backends.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(user_id=username)  # 'user_id' 필드에 맞게 변경
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
