from django.db import models

class Person(models.Model):
    class Meta:
        unique_together = ('name', 'address',)
        
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self) -> str:
        return f"{str(self.name)}"