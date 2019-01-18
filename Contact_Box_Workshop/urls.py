"""Contact_Box_Workshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from Contact_Box_App.views import (
    PersonListView,
    PersonDetailView,
    PersonCreateView,
    PersonUpdateView,
    PersonDeleteView,
    AddressCreateView,
    PhoneCreateView,
    PhoneDeleteView,
    EmailCreateView,
    EmailDeleteView,
    GroupListView,
    GroupCreateView,
    GroupDetailView,
    GroupDeleteView
)

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^$', PersonListView.as_view(), name='person-list-view'),
    url(r'^new/$', PersonCreateView.as_view(), name='person-create-view'),
    url(r'^show/(?P<id>(\d)+)/$', PersonDetailView.as_view(), name='person-detail-view'),
    url(r'^modify/(?P<id>(\d)+)/$', PersonUpdateView.as_view(), name='person-update-view'),
    url(r'delete/(?P<id>(\d)+)/$', PersonDeleteView.as_view(), name='person-delete-view'),
    url(r'^(?P<id>(\d)+)/addAddress/$', AddressCreateView.as_view(), name='address-create-view'),
    url(r'^(?P<id>(\d)+)/addPhone/$', PhoneCreateView.as_view(), name='phone-create-view'),
    url(r'^delete-phone/(?P<id>(\d)+)/$', PhoneDeleteView.as_view(), name='phone-delete-view'),
    url(r'^(?P<id>(\d)+)/addEmail/$', EmailCreateView.as_view(), name='email-create-view'),
    url(r'^delete-email/(?P<id>(\d)+)/$', EmailDeleteView.as_view(), name='email-delete-view'),
    url(r'^groups/$', GroupListView.as_view(), name='group-list-view'),
    url(r'^addGroup$', GroupCreateView.as_view(), name='group-create-view'),
    url(r'^showGroup/(?P<id>(\d)+)/$', GroupDetailView.as_view(), name='group-detail-view'),
    url(r'^delete-group/(?P<id>(\d)+)/$', GroupDeleteView.as_view(), name='group-delete-view')

]
