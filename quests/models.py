from django.db import models


class CreateQuestboard(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    stars = models.IntegerField()

    def get_absolute_url(self):
        return reverse('edit', args=[str(self.pk)])