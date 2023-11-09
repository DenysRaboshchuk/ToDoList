from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(
        max_length=255
    )


class Task(models.Model):
    content = models.TextField()
    datetime_field = models.DateTimeField(
        auto_now_add=True
    )
    deadline = models.DateTimeField(
        blank=True,
        null=True,
    )
    task_done = models.BooleanField(
        default=False,
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="tags",
    )


