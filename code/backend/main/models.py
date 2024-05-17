from django.db import models


class Application(models.Model):
    type = models.CharField(max_length=100)
    budget = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    client_contact = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.client_name} {self.client_contact}"