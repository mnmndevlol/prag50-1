from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    def form_valid(self, form): #forms.py에서 리퀘스트로 날아온 폼 데이터가 여기 두번째인자의 form안에 있다.
        temp_profile = form.save(commit=False) # 아직 저장은 안하고 임시 대기중인 데이터로 임시저장.
        temp_profile.user = self.request.user # 리퀘스트를 보낸 당사자를 추가적으로 담아서
        temp_profile.save() # 그렇게 합쳐진걸 최종적으로 저장함.
        return super().form_valid(form) #그리고 몇글자 이상 뭐 그런거 유효성검사하고 다시 응답해주고 그러는것같다.

    def get_success_url(self):
        return reverse('accountapp:detail',
                       kwargs={'pk': self.object.user.pk}) # 여기서 self.object가 의미하는건 model=Profile 부분.

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail',
                       kwargs={'pk': self.object.user.pk})