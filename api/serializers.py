from rest_framework import serializers
from .models import JournalEntry

class JournalEntrySerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = JournalEntry
        fields = ('id', 'date', 'title', 'content', 'rating')