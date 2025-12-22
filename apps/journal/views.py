from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib import messages

from .models import JournalEntry
from .forms import JournalEntryForm


@login_required
def journal_list(request):
    entries = JournalEntry.objects.filter(
        user=request.user,
        deleted_at__isnull=True
    ).order_by("-created_at")

    return render(
        request,
        "journal/journal_list.html",
        {"entries": entries}
    )


@login_required
def journal_create(request):
    if request.method == "POST":
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            # ✅ FIXED REDIRECT
            return redirect("journal:list")
    else:
        form = JournalEntryForm()

    recent_entries = JournalEntry.objects.filter(
        user=request.user,
        deleted_at__isnull=True,
        created_at__gte=timezone.now() - timedelta(days=7)
    ).order_by("-created_at")

    return render(
        request,
        "journal/journal_form.html",
        {
            "form": form,
            "recent_entries": recent_entries,
        }
    )


@login_required
@require_POST
def journal_delete(request, entry_id):
    entry = get_object_or_404(
        JournalEntry,
        id=entry_id,
        user=request.user,
        deleted_at__isnull=True
    )
    entry.soft_delete()
    request.session["last_deleted_journal_id"] = entry.id
    return redirect("journal:list")


@login_required
@require_POST
def journal_restore(request):
    entry_id = request.session.pop("last_deleted_journal_id", None)

    if not entry_id:
        messages.info(request, "There is no journal entry to restore.")
        return redirect("journal:list")

    try:
        entry = JournalEntry.objects.get(
            id=entry_id,
            user=request.user,
            deleted_at__isnull=False
        )
    except JournalEntry.DoesNotExist:
        messages.warning(
            request,
            "That journal entry can no longer be restored."
        )
        return redirect("journal:list")

    entry.restore()
    messages.success(request, "Journal entry restored.")
    return redirect("journal:list")


@login_required
def journal_trash(request):
    entries = JournalEntry.objects.filter(
        user=request.user,
        deleted_at__isnull=False
    ).order_by("-deleted_at")

    return render(
        request,
        "journal/journal_trash.html",
        {"entries": entries}
    )


@login_required
@require_POST
def journal_hard_delete(request, entry_id):
    entry = get_object_or_404(
        JournalEntry,
        id=entry_id,
        user=request.user,
        deleted_at__isnull=False
    )
    entry.delete()
    return redirect("journal:trash")
