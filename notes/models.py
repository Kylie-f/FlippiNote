from django.db import models

class Note(models.Model):
    body = models.TextField()

    def __str__(self):
        return self.body
