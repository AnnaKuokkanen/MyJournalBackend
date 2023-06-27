from rest_framework import viewsets
from .serializers import JournalEntrySerializer
from .models import JournalEntry


class JournalEntriesViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all().order_by('date')
    serializer_class = JournalEntrySerializer