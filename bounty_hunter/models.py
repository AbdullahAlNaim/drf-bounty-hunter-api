from django.db import models

# Create your models here.
class Creature(models.Model):
    DIFFICULTY_CHOICE = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('very-high', 'Very-High')
    ]
    task = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)