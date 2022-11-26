from django.db import models
from django.utils import timezone

# Create your models here.
class JournalEntry(models.Model): 
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    title = models.TextField(max_length=50, null=True)
    content = models.TextField(null=True)
    rating = models.IntegerField(default=0)
