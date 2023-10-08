from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView
from scheduling_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/', permanent=True)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('settings/', views.settings, name='settings'),
    path('organizer/', views.organizer, name='organizer'),
    path('participant/', views.participant, name='participant'),
    path('edit_event/', views.edit_event, name='edit_event'),
    path('<str:event_code>/', views.published_event, name='published_event'),
]
