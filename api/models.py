from django.db import models
from django.utils import timezone, dateformat
# Create your models here.
class JournalEntry(models.Model): 
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(default=dateformat.format(timezone.now(), 'Y-m-d'))
    title = models.TextField(max_length=50, null=True)
    content = models.TextField(null=True)
    rating = models.PositiveIntegerField(default=0)
