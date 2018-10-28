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
from django.urls import path
from Contact_Box_App.views import PersonListView, \
                                  PersonDetailView, \
                                  PersonCreateView, \
                                  PersonUpdateView, \
                                  PersonDeleteView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PersonListView.as_view(), name='person-list-view'),
    path('show/<int:id>', PersonDetailView.as_view(), name='person-detail-view'),
    path('new/', PersonCreateView.as_view(), name='person-create-view'),
    path('modify/<int:id>', PersonUpdateView.as_view()),
    path('delete/<int:id>', PersonDeleteView.as_view()),



]
