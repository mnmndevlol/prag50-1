from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk']) # pk가 urls에서 업데이트로 받는 pk가 pk를 받아서 프로파일의 주인을 확인하고
        if not profile.user == request.user: #프로파일의 유저와 리퀘스를 보내는 유저가 같지 않다면
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated