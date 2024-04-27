from django.urls import include, path

from users import views
from users.views import Register

urlpatterns = [
    path('',include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),
    path('vote/', views.vote, name='vote'),
    path('profile/', views.profile, name='profile'),
]