from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('tprofile/', views.tprofile, name='tprofile'),
    path('person/', views.person, name='person'),
    path('studyplan/', views.studyplan, name='studyplan')
]
