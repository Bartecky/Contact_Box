from django.shortcuts import get_object_or_404, reverse, render, HttpResponseRedirect, redirect
from django.urls import reverse_lazy
from .models import Person, Group, Phone, Email
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .forms import (
    PersonModelForm,
    PersonUpdateForm,
    AddressModelForm,
    PhoneModelForm,
    EmailModelForm,
    GroupModelForm,
    AddingPersonToGroupForm
)
from django.contrib import messages
from django.db.models import Q


# Create your views here.


class PersonListView(ListView):
    template_name = 'person-list-view.html'
    queryset = Person.objects.all().order_by('surname')
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        qs = Person.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(surname__icontains=query) |
                Q(name__icontains=query)
            )
        return qs


class PersonDetailView(DetailView):
    template_name = 'person-detail-view.html'

    def get_object(self, queryset=None):
        _id = self.kwargs.get('id')
        return get_object_or_404(Person, id=_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        groups = Group.objects.all()
        context['groups'] = groups
        return context


class PersonCreateView(CreateView):
    template_name = 'person-create-view.html'
    form_class = PersonModelForm


class PersonUpdateView(View):

    def get(self, request, id):
        person = Person.objects.get(id=id)
        form = PersonUpdateForm(instance=person, initial={'phone': person.phone_set.first(),
                                                          'email': person.email_set.first()})
        return render(request, 'person-update-view.html', {'form': form})

    def post(self, request, id):
        form = PersonUpdateForm(request.POST or None)
        ctx = {
            'form': form
        }
        if form.is_valid():
            person = Person.objects.get(id=id)
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            address = form.cleaned_data['address']
            description = form.cleaned_data['description']
            person.name = name
            person.surname = surname
            person.address = address
            person.description = description
            person.save()
            return HttpResponseRedirect(reverse('person-detail-view', kwargs={'id': person.id}))
        return reverse('person-detail-view', kwargs={'id': self.kwargs.get('id')})


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        person = Person.objects.get(id=self.kwargs.get('id'))
        context['person'] = person
        return context

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
        id = self.kwargs.get('id')
        phone = Phone.objects.get(id=id)
        return reverse('person-detail-view', kwargs={'id': phone.person.id})


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
        id = self.kwargs.get('id')
        email = Email.objects.get(id=id)
        return reverse('person-detail-view', kwargs={'id': email.person.id})


class GroupListView(ListView):
    template_name = 'group-list-view.html'
    queryset = Group.objects.all().order_by('name')
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        qs = Group.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query)
            )
        return qs


class GroupCreateView(CreateView):
    template_name = 'group-create-view.html'
    form_class = GroupModelForm


class GroupDetailView(DetailView):
    template_name = 'group-detail-view.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Group, id=id_)


class GroupUpdateView(UpdateView):
    queryset = Group.objects.all()
    form_class = GroupModelForm
    template_name = 'group-update-view.html'


class GroupDeleteView(DeleteView):
    template_name = 'group-delete-view.html'

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Group, id=id_)

    def get_success_url(self):
        return reverse('group-list-view')


class AddingPersonToGroup(View):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        person = Person.objects.get(id=id)
        form = AddingPersonToGroupForm(initial={'person': person})
        ctx = {
            'form': form
        }
        return render(request, 'adding-person-to-group-view.html', ctx)

    def post(self, request, id):
        form = AddingPersonToGroupForm(request.POST or None)
        if form.is_valid():
            person = Person.objects.get(id=id)
            group = form.cleaned_data['groups']
            person.group_set.set(group)
            person.save()
            return redirect(reverse_lazy('person-list-view'))
        return render(request, 'adding-person-to-group-view.html', {'form': form})


class RemovePersonFromGroup(View):
    def get(self, request, *args, **kwargs):
        group_id = self.kwargs.get('id')
        person_id = self.kwargs.get('person_id')
        group = Group.objects.get(id=group_id)
        obj_person = Person.objects.get(id=person_id)
        group.person.remove(obj_person)
        group.save()
        messages.success(request, '{}'.format('Removed'))
        return redirect(reverse('group-detail-view', kwargs={'id': group_id}))
