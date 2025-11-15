from django.db import models


class UserData(models.Model):
    account_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    requested_url = models.TextField()

    def __str__(self):
        return f"{self.username} | {self.account_name}"
