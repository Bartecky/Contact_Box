from django.shortcuts import get_object_or_404, reverse
from .models import Person, Groups, Phone, Email
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PersonModelForm, AddressModelForm, PhoneModelForm, EmailModelForm, GroupsModelForm


# Create your views here.

class PersonListView(ListView):
    template_name = 'person-list-view.html'
    queryset = Person.objects.all().order_by('surname')


class PersonDetailView(DetailView):
    template_name = 'person-detail-view.html'

    def get_object(self, queryset=None):
        _id = self.kwargs.get('id')
        return get_object_or_404(Person, id=_id)


class PersonCreateView(CreateView):
    template_name = 'person-create-view.html'
    form_class = PersonModelForm


class PersonUpdateView(UpdateView):
    template_name = 'person-update-view.html'
    form_class = PersonModelForm

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Person, id=id_)


class PersonDeleteView(DeleteView):
    template_name = 'person-delete-view.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Person, id=id_)

    def get_success_url(self):
        return reverse('person-list-view')


class AddressCreateView(CreateView):
    template_name = 'address-create-view.html'
    form_class = AddressModelForm

    def form_valid(self, form):
        _id = self.kwargs.get('id')
        person = get_object_or_404(Person, id=_id)
        person.address = form.save()
        person.save()
        return super(AddressCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('person-detail-view', kwargs={'id': self.kwargs.get('id')})


class PhoneCreateView(CreateView):
    template_name = 'phone-create-view.html'
    form_class = PhoneModelForm

    def form_valid(self, form):
        person = get_object_or_404(Person, id=self.kwargs.get('id'))
        form.instance.person = person
        return super(PhoneCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['person'] = get_object_or_404(Person, pk=self.kwargs.get('id'))
        return context

    def get_initial(self):
        return {
            'person': get_object_or_404(Person, pk=self.kwargs.get('id'))
        }

    def get_success_url(self):
        return reverse('person-detail-view', kwargs={'id': self.kwargs.get('id')})


class PhoneDeleteView(DeleteView):
    template_name = 'phone-delete-view.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Phone, id=id_)

    def get_success_url(self):
        return reverse('person-list-view')


#
class EmailCreateView(CreateView):
    template_name = 'email-create-view.html'
    form_class = EmailModelForm

    def form_valid(self, form):
        person = get_object_or_404(Person, id=self.kwargs.get('id'))
        form.instance.person = person
        return super(EmailCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['person'] = get_object_or_404(Person, pk=self.kwargs.get('id'))
        return context

    def get_initial(self):
        return {
            'person': get_object_or_404(Person, pk=self.kwargs.get('id'))
        }

    def get_success_url(self):
        return reverse('person-detail-view', kwargs={'id': self.kwargs.get('id')})


class EmailDeleteView(DeleteView):
    template_name = 'email-delete-view.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Email, id=id_)

    def get_success_url(self):
        return reverse('person-list-view')


class GroupsListView(ListView):
    template_name = 'group-list-view.html'
    queryset = Groups.objects.all().order_by('name')


class GroupCreateView(CreateView):
    template_name = 'group-create-view.html'
    form_class = GroupsModelForm


class GroupDetailView(DetailView):
    template_name = 'group-detail-view.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Groups, id=id_)


class GroupDeleteView(DeleteView):
    template_name = 'group-delete-view.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Groups, id=id_)

    def get_success_url(self):
        return reverse('groups-list-view')
