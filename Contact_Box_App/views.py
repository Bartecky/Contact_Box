from django.shortcuts import render, get_object_or_404, reverse
from .models import  Person, Groups
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PersonModelForm


# Create your views here.

class PersonListView(ListView):
    template_name = 'person-list-view.html'
    queryset = Person.objects.all().order_by('surname')


class PersonDetailView(DetailView):
    template_name = 'person-detail-view.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Person, id=id_)


class PersonCreateView(CreateView):
    template_name = 'person-create-view.html'
    form_class = PersonModelForm




class PersonUpdateView(UpdateView):
    template_name = 'person-update-view.html'
    form_class = PersonModelForm

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Person, id=id_)

    def get_success_url(self):
        return reverse('person-list-view')


class PersonDeleteView(DeleteView):
    template_name = 'person-delete-view.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Person, id=id_)

    def get_success_url(self):
        return reverse('person-list-view')

