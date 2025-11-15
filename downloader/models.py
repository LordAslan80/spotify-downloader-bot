from django.db import models


class UserData(models.Model):
    account_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    requested_url = models.TextField()

    def __str__(self):
        return f"{self.username} | {self.account_name}"
