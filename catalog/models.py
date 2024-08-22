from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(blank=True, default=False)
    tags = models.ManyToManyField(to="Tag", related_name="tasks")

    class Meta:
        ordering = (
            "is_done",
            "-created_at",
        )

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name
