from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):

    def __str__(self):
        return self.title

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images', default="images/default.jpg")
    page_count = models.PositiveIntegerField(null=True, blank=True)
    recommended_by = models.CharField(max_length=200, null=True, blank=True)
    series_name = models.CharField(max_length=200, null=True, blank=True)
    series_number = models.PositiveIntegerField(null=True, blank=True)
    owned = models.BooleanField()
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    READ_STATUS_CHOICES = [
        ("NOT_STARTED", "Not_Started"),
        ("IN_PROGRESS", "In_Progress"),
        ("FINISHED", "Finished")
    ]
    read_status = models.CharField(max_length=12, choices=READ_STATUS_CHOICES, default="NOT_STARTED")
    rating = models.FloatField(
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(5.0),
            MinValueValidator(0.0)
        ]
    )
    notes = models.TextField(null=True, blank=True)
    date_started = models.DateField(null=True, blank=True)
    date_finished = models.DateField(null=True, blank=True)
    times_read = models.PositiveIntegerField(null=True, blank=True)
