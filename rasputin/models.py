from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    host = models.ForeignKey("Users", on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey("Topic", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    # participants = models.ManyToManyField("Users")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Users(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    