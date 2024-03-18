from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Group(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Student(models.Model):
    student_name = models.CharField(max_length=60)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name
