from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=200)
    nomber = models.IntegerField(default=0)
    power = models.IntegerField(default=0)
    image = models.CharField(max_length=200)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.nomber + " " + self.name + ", puissance " + self.power
