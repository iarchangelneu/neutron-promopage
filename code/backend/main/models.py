from django.db import models
from send_tg import send_message


class Application(models.Model):
    client_name = models.CharField(max_length=100)
    client_contact = models.CharField(max_length=100)
    type = models.CharField(max_length=100, blank=True)
    budget = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.client_name} {self.client_contact}"
    
    def save(self, *args, **kwargs):
        send_message(
            f"Новая заявка!!! @IlyaSushinб @iarchangelmkn\n\n"
            f"Имя: {self.client_name}\n"
            f"Телефон: {self.client_name}\n"
            f"Тип: {self.type}\n"
            f"Бюджет: {self.budget}\n"
            f"Комент: {self.comment}\n"
        )
        super(Application, self).save(*args, **kwargs)