from django.urls import path, include

# Wire up Django's built-in auth views (login, logout, password management).
# Templates should live under `users/templates/registration/` (login.html etc.).
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]
