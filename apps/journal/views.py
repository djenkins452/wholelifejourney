from datetime import timezone as dt_timezone

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils import timezone
from zoneinfo import ZoneInfo

from .models import JournalEntry
from .forms import JournalEntryForm


# --------------------------------------------------
# Journal List
# --------------------------------------------------

@login_required
def journal_list(request):
    entries = JournalEntry.objects.filter(
        user=request.user,
        deleted_at__isnull=True
    ).order_by("-entry_date")

    hidden_count = JournalEntry.objects.filter(
        user=request.user,
        deleted_at__isnull=False
    ).count()

    return render(
        request,
        "journal/journal_list.html",
        {
            "entries": entries,
            "hidden_count": hidden_count,
            "show_form": False,
        }
    )


# --------------------------------------------------
# Create Entry
# --------------------------------------------------

@login_required
def journal_create(request):
    if request.method == "POST":
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user

            # -------------------------------
            # TITLE FORMATTING (PHASE B)
            # -------------------------------
            raw_title = (form.cleaned_data.get("title") or "").strip()
            entry_date = form.cleaned_data["entry_date"]

            formatted_date = entry_date.strftime("%A, %b %d, %Y")

            if raw_title:
                entry.title = f"{raw_title} - {formatted_date}"
            else:
                entry.title = formatted_date

            entry.save()
            messages.success(request, "Journal entry saved.")
            return redirect("journal:list")
    else:
        # Default entry_date to user's local time
        try:
            user_tz = ZoneInfo(request.user.profile.timezone)
        except Exception:
            user_tz = dt_timezone.utc

        local_now = timezone.now().astimezone(user_tz)

        form = JournalEntryForm(
            initial={
                "entry_date": local_now.replace(second=0, microsecond=0),
                "title": "",
            }
        )

    entries = JournalEntry.objects.filter(
        user=request.user,
        deleted_at__isnull=True
    ).order_by("-entry_date")

    hidden_count = JournalEntry.objects.filter(
        user=request.user,
        deleted_at__isnull=False
    ).count()

    return render(
        request,
        "journal/journal_list.html",
        {
            "form": form,
            "entries": entries,
            "hidden_count": hidden_count,
            "show_form": True,
        }
    )


# --------------------------------------------------
# Edit Entry (UNCHANGED)
# --------------------------------------------------

@login_required
def journal_edit(request, entry_id):
    entry = get_object_or_404(
        JournalEntry,
        id=entry_id,
        user=request.user,
        deleted_at__isnull=True
    )

    if request.method == "POST":
        form = JournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, "Journal entry updated.")
            return redirect("journal:list")
    else:
        form = JournalEntryForm(instance=entry)

    entries = JournalEntry.objects.filter(
        user=request.user,
        deleted_at__isnull=True
    ).order_by("-entry_date")

    hidden_count = JournalEntry.objects.filter(
        user=request.user,
        deleted_at__isnull=False
    ).count()

    return render(
        request,
        "journal/journal_list.html",
        {
            "form": form,
            "entries": entries,
            "hidden_count": hidden_count,
            "show_form": True,
            "editing": True,
            "editing_entry": entry,
        }
    )


# --------------------------------------------------
# Hide (Soft Delete)
# --------------------------------------------------

@login_required
@require_POST
def journal_delete(request, entry_id):
    entry = get_object_or_404(
        JournalEntry,
        id=entry_id,
        user=request.user
    )
    entry.soft_delete()
    return redirect("journal:list")


# --------------------------------------------------
# Permanent Delete
# --------------------------------------------------

@login_required
@require_POST
def journal_hard_delete(request, entry_id):
    entry = get_object_or_404(
        JournalEntry,
        id=entry_id,
        user=request.user
    )
    entry.delete()
    return redirect("journal:list")


# --------------------------------------------------
# Hidden Entries (Trash)
# --------------------------------------------------

@login_required
def journal_trash(request):
    entries = JournalEntry.objects.filter(
        user=request.user,
        deleted_at__isnull=False
    ).order_by("-deleted_at")

    return render(
        request,
        "journal/journal_trash.html",
        {
            "entries": entries,
        }
    )


# --------------------------------------------------
# Restore Hidden Entry
# --------------------------------------------------

@login_required
@require_POST
def journal_restore(request, entry_id):
    entry = get_object_or_404(
        JournalEntry,
        id=entry_id,
        user=request.user,
        deleted_at__isnull=False
    )
    entry.restore()
    return redirect("journal:trash")
