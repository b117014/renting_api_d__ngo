from django.db import models
# Create your models here.


# class User(models.Model):

#     name = models.CharField(max_length=64)
#     email = models.EmailField()
#     username = models.CharField(max_length=64)
#     password = models.CharField(max_length=20)

class Message(models.Model):

    title = models.CharField(max_length=64)
    text = models.TextField()

    def __str__(self):
        return f"{self.text} and {self.title}"
