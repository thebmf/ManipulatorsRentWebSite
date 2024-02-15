from django.db import models
from django.urls import reverse


class RequestManipulator(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"Заявка от {self.name}"

    def get_absolute_url(self):
        return reverse("index")
