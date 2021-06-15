from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True) # 셋팅스에서 MEDIA_ROOT를 media로 해줬으니 /media/profile/ 이렇게 되는거
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)







