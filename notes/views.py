from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def index(request):
    notes = Note.objects.all()
    return render(request, 'index.html', {'notes': notes})


def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('detail', pk=note.pk)
    else:
        form = NoteForm()
        return render(request, 'create.html', {'form': form})


def detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'detail.html', {'note': note})


def update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            return redirect('detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'update.html', {'form': form})


def delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('index')
