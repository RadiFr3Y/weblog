from django.shortcuts import render, redirect
from webapp.models import PostModel
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .mixins import FieldsMixin, FormValidMixin, AuthoraccessMixin, SuperuserAccessMixin
from .models import User
from .forms import ProfileForm
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


@login_required
def PostList(request):
    def get_queryset():
        if request.user.is_superuser:
            return PostModel.objects.all()
        else:
            return PostModel.objects.filter(author=request.user)
    context ={
        'article': get_queryset(),
        'post': PostModel.objects.all()
    }
    return render(request, 'registration/home.html', context)


class PostCreate(LoginRequiredMixin, FormValidMixin, FieldsMixin, CreateView):
    model = PostModel
    template_name = "registration/Post-create-update.html"

class PostUpdate(AuthoraccessMixin, FormValidMixin, FieldsMixin, UpdateView):
    model = PostModel
    template_name = "registration/Post-create-update.html"

class PostDelet(SuperuserAccessMixin, DeleteView):
    model = PostModel
    success_url = reverse_lazy('account:home')
    template_name = 'registration/postmodel_confirm_delete.html'

def Logout(request):
    if request.method == "POST":
        logout(request)
    return redirect('login')

class Profile(UpdateView):
    template_name = "registration/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy('account:profile')
    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account!'
            message = render_to_string('registration/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'registration/signup_sended_email.html')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'registration/activate_true.html')
    else:
        return render(request, 'registration/activate_false.html')