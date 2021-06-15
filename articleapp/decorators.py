from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk']) # pk에 해당하는 아티클을 찾아서
        if not article.writer == request.user:  # 아티클의 writer가 리퀘스트를 보내는 유저와 같지 않다면
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated

