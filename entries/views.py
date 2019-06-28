from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Entry
from django.utils import timezone
from .forms import EntryForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def entry_list(request):
  entries = Entry.objects.filter(author=request.user.id).order_by('-created_date') #filter(author=request.user.title)
  return render(request, 'entries/entry_list.html', {'entries': entries})

# @login_required
def entry_detail(request, pk):
  entry = get_object_or_404(Entry, pk=pk)
  return render(request, 'entries/entry_detail.html', {'entry': entry})

@login_required
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

@login_required
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

@login_required
def post_remove(request, pk):
  entry = get_object_or_404(Entry, pk=pk)
  entry.delete()
  return redirect('entry_list')

# Register user
def signup(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('entry_list')
  form = SignUpForm()
  return render(request, 'registration/signup.html', {'form': form})

