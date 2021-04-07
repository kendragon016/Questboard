from django.contrib.postgres.fields import ArrayField
from django.db import models


class Questboard(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=280)
    stars = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Quest(models.Model):
    board = models.ForeignKey(
        Questboard,
        on_delete=models.CASCADE,
        related_name='course',
        default=0
        )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=280)
    stars = models.IntegerField()
    everyone = models.BooleanField(default=False)
    sign_ups = ArrayField(
        models.CharField(max_length=50),
        blank=True,
        null=True,
        size=3
        )

    def __str__(self):
        return f"{self.board.name}: {self.name}"
