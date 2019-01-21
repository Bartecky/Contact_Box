from django import forms
from .models import Person, Address, Phone, Email, Group


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'surname',
            'description',
        ]


class AddressModelForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class PhoneModelForm(forms.ModelForm):
    number = forms.IntegerField()

    class Meta:
        model = Phone
        fields = [
            'number',
            'type',
        ]

    def clean_number(self):
        number = self.cleaned_data['number']
        if len(str(number)) != 9:
            raise forms.ValidationError('Number must be nine-digit')
        return number


class PersonUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'surname',
            'description',
            'address',
        ]


class EmailModelForm(forms.ModelForm):
    person = forms.ModelChoiceField(queryset=Person.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Email
        fields = [
            'address',
            'type',
            'person'
        ]


class GroupModelForm(forms.ModelForm):
    person = forms.ModelMultipleChoiceField(queryset=Person.objects.all(),
                                            widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Group
        fields = '__all__'
