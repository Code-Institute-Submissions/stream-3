from django.db import models
from django.core.validators import URLValidator

LOCATION_CHOICES = (
    ('Leinster', 'Leinster'),
    ('Ulster', 'Ulster'),
    ('Munster', 'Munster'),
    ('Connacht', 'Connacht'),
)

TYPE_CHOICES = (
    ('Wedding Band', 'Wedding Band'),
    ('DJ', 'DJ'),
)

class Entertainer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    bio = models.TextField()
    entertainer_type = models.CharField(choices=TYPE_CHOICES, default='Wedding Band', max_length=300)
    location = models.CharField(choices=LOCATION_CHOICES, default='Leinster', max_length=300)
    facebook = models.CharField(validators=[URLValidator()], max_length=300)
    twitter = models.CharField(validators=[URLValidator()], max_length=300)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.name
