from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(user=user,
                                                   project=project)
        # 있으면 없애고 없으면 만들고 그런 방식
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    # 아티클에 있는 특정 조건을 가진 게시글들만 가지고와야하기때문에 쿼리셋을 작성함.
    # 가지고오는 조건을 바꿀 수 있다
    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project') # values_list는 값들을 리스트화 시켜서 담겠다는 것
        article_list = Article.objects.filter(project__in=projects)
        return article_list