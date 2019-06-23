from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Entry
from django.utils import timezone
from .forms import EntryForm
from django.shortcuts import redirect


def entry_list(request):
  entries = Entry.objects.order_by('-created_date')
  return render(request, 'entries/entry_list.html', {'entries': entries})

def entry_detail(request, pk):
  entry = get_object_or_404(Entry, pk=pk)
  return render(request, 'entries/entry_detail.html', {'entry': entry})

def post_new(request):
  if request.method == "POST":
    form = EntryForm(request.POST)
    if form.is_valid():
      entry = form.save(commit=False)
      entry.author = request.user
      entry.save()
      return redirect('entry_detail', pk=entry.pk)
  else:
    form = EntryForm()
  return render(request, 'entries/post_edit.html', {'form': form})

def post_edit(request, pk):
  entry = get_object_or_404(Entry, pk=pk)
  if request.method == "POST":
    form = EntryForm(request.POST, instance=entry)
    if form.is_valid():
      entry = form.save(commit=False)
      entry.author = request.user
      entry.save()
      return redirect('entry_detail', pk=entry.pk)
  else:
    form = EntryForm(instance=entry)
  return render(request, 'entries/post_edit.html', {'form': form})





