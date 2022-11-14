from django.db import models
from django.utils import timezone

# Create your models here.
class JournalEntry(models.Model): 
    id = models.BigAutoField(primary_key=True)
    content = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)
