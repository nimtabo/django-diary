from django.shortcuts import render

# Create your views here.
from .models import Entry
from django.utils import timezone


def entry_list(request):
  entries = Entry.objects.order_by('-created_date')
  return render(request, 'entries/entry_list.html', {'entries': entries})