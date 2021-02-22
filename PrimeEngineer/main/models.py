from django.db import models

# Create your models here.
class Works(models.Model):
    Name = models.CharField(max_length = 200)
    Description = models.TextField()
    PublishDate = models.DateTimeField("Published date")
    domaine = models.CharField(max_length = 70)
    photo = models.BinaryField()

    def __str__(self):
        return self.Name