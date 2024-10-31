from django.db import models
from cats.models import SpyCat


class Target(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Mission(models.Model):
    cat = models.ForeignKey(SpyCat, on_delete=models.CASCADE)
    targets = models.ManyToManyField(
        Target
    )  # One mission can have multiple goals, and one goal can be in multiple missions
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Mission for {self.cat.name}"
