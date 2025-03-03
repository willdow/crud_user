from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class UserListView(ListView):
    model = CustomUser
    template_name = 'users/list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'users/show.html'
    context_object_name = 'user_obj'

class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/form.html'
    success_url = reverse_lazy('user-list')

class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/form.html'
    
    def get_success_url(self):
        return reverse_lazy('user-detail', kwargs={'pk': self.object.pk})

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'users/confirmation.html'
    success_url = reverse_lazy('user-list')