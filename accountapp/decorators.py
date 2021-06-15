from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

# 겟이나 포스트나 요청을 받을 때 마다 그 pk를 사용해서 그 유저리퀘스트가 실제로 요청을 보낸 유저와 같은지 확인
def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk']) # 요청을 받으면서 pk로 받은 값을 가지고있는 유저 오브젝트
        if not user == request.user: # 받은 리퀘스트의 유저가 아니라면 권한없다는 리턴
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated