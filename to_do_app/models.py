from django.db import models


class Tag(models.Model):
    name = models.TextField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["done", "-datetime"]
