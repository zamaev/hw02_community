from django.urls import reverse_lazy  # позволяет получать url по path
from django.views.generic.edit import CreateView

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'
