from django.db import models
from django.urls import reverse


# Create your models here.

class Address(models.Model):
    city = models.CharField(max_length=32, null=True, blank=True)
    street = models.CharField(max_length=32, null=True, blank=True)
    house_number = models.IntegerField(null=True, blank=True)
    flat_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{}, ul.{} {} {}'.format(self.city, self.street, self.house_number, self.flat_number)

    def get_absolute_url(self):
        return reverse('person-detail-view', kwargs={'id': self.id})

    class Meta:
        verbose_name_plural = 'Addresses'


class Person(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

    def get_absolute_url(self):
        return reverse('person-detail-view', kwargs={'id': self.id})


class Phone(models.Model):
    number = models.IntegerField(unique=True, null=True, blank=True)
    type = models.CharField(max_length=32, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.number)

    def get_absolute_url(self):
        return reverse('person-detail-view', kwargs={'id': self.id})


class Email(models.Model):
    address = models.EmailField(max_length=32, unique=True, null=True, blank=True)
    type = models.CharField(max_length=32, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.address)


class Group(models.Model):
    name = models.CharField(max_length=32)
    person = models.ManyToManyField(Person)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('group-detail-view', kwargs={'id': self.id})
