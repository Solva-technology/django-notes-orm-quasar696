from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Note, User


def note_list(request):
    template_name = 'note_list.html'
    notes = Note.objects.select_related(
        "author", "status").prefetch_related("categories")
    context = {'notes': notes}
    return render(request, template_name, context)


def note_detail(request, note_id):
    template_name = 'note_detail.html'
    note = get_object_or_404(Note, id=note_id)
    context = {'note': note}
    return render(request, template_name, context)


def user_detail(request, user_id):
    template_name = "user_detail.html"
    user = get_object_or_404(User, id=user_id)
    notes = user.note_set.select_related("status").all()
    context = {
        "user": user,
        "notes": notes
    }
    return render(request, template_name, context)
