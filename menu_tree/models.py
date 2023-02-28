from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=100, blank=True, null=True, unique=True)
    named_url = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name
