from django.urls import path, include
from django.views.generic import TemplateView

# Wire up Django's built-in auth views (login, logout, password management).
# Also provide a simple profile page so templates that reverse 'profile'
# (e.g. navbar) will resolve. Replace with a real view when implementing
# user profiles.
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', TemplateView.as_view(template_name='profile/profile.html'), name='profile'),
]
