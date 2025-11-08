from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
	"""Minimal custom user model used as AUTH_USER_MODEL.

	Kept intentionally minimal to match the project's expectations that a
	`users.UserProfile` exists. Add extra fields here later as needed.
	"""
	# Example extra field (uncomment if needed):
	# phone = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self) -> str:  # pragma: no cover - trivial
		return self.username
