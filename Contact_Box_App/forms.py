from django import forms
from .models import Person, Address, Phone, Email, Groups


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


class EmailModelForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = [
            'address',
            'type',
            'person'
        ]


class GroupsModelForm(forms.ModelForm):
    person = forms.ModelMultipleChoiceField(queryset=Person.objects.all(),
                                            widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Groups
        fields = '__all__'
