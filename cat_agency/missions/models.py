from django.db import models
from cats.models import SpyCat

class Mission(models.Model):
    cat = models.OneToOneField(SpyCat, null=True, blank=True, on_delete=models.CASCADE)  # One cat - one mission
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Mission for {self.cat.name}"
    

class Target(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='targets')
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    complete = models.BooleanField(default=False)

    class Meta:
        unique_together = ('mission', 'name')  # A unique combination for purpose and mission

    def __str__(self):
        return self.name