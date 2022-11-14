from django.db import models
from django.utils import timezone

# Create your models here.
class JournalEntry(models.Model): 
    id = models.CharField(max_length=50, primary_key=True)
    content = models.TextField(null=True)
    date = models.DateField(default=timezone.now)
