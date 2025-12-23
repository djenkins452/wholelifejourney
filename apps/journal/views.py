from datetime import timedelta
from datetime import timezone as dt_timezone

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.utils import timezone
from zoneinfo import ZoneInfo

from .models import JournalEntry
from .forms import JournalEntryForm


def _get_user_tz(request):
    try:
        return ZoneInfo(request.user.profile.timezone)
    except Exception:
        return dt_timezone.utc


def _attach_local_display_fields(entries, user_tz):
    """
    Presentation-only fields. No DB writes.
    - entry.local_dt
    - entry.local_date
    - entry.display_date
    - entry.display_title (strips redundant ' - {date}' suffix if present)
    """
    for entry in entries:
        local_dt = entry.entry_date.astimezone(user_tz)
        local_date = local_dt.date()

        date_str = local_date.strftime("%A, %b %d, %Y")
        raw_title = (entry.title or "").strip()

        suffix = f" - {date_str}"
        if raw_title.endswith(suffix):
            display_title = raw_title[: -len(suffix)].strip()
        elif raw_title == date_str:
            display_title = ""
        else:
            display_title = raw_title

        entry.local_dt = local_dt
        entry.local_date = local_date
        entry.display_date = date_str
        entry.display_title = display_title


def _build_grouped_context(request):
    """
    Builds the journal listing context with:
    - grouped_entries (by user's local day)
    - total_count
    - hidden_count
    """
    user_tz = _get_user_tz(request)

    now_local = timezone.now().astimezone(user_tz)
    today = now_local.date()
    yesterday = today - timedelta(days=1)

    entries_qs = (
        JournalEntry.objects
        .filter(user=request.user, deleted_at__isnull=True)
        .order_by("-entry_date")
    )

    total_count = entries_qs.count()

    # Evaluate queryset once; attach display fields for template
    entries = list(entries_qs)
    _attach_local_display_fields(entries, user_tz)

    groups = {}
    for entry in entries:
        local_date = entry.local_date

        if local_date == today:
            label = "Today"
        elif local_date == yesterday:
            label = "Yesterday"
        else:
            label = local_date.strftime("%A, %b %d, %Y")

        if local_date not in groups:
            groups[local_date] = {"label": label, "entries": []}

        groups[local_date]["entries"].append(entry)

    grouped_entries = [groups[d] for d in sorted(groups.keys(), reverse=True)]

    hidden_count = JournalEntry.objects.filter(
        user=request.user,
        deleted_at__isnull=False
    ).count()

    return {
        "grouped_entries": grouped_entries,
        "total_count": total_count,
        "hidden_count": hidden_count,
    }


# --------------------------------------------------
# Journal List
# --------------------------------------------------

@login_required
def journal_list(request):
    context = _build_grouped_context(request)
    context.update({"show_form": False})
    return render(request, "journal/journal_list.html", context)


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

            raw_title = (form.cleaned_data.get("title") or "").strip()
            entry_date = form.cleaned_data["entry_date"]

            # Phase D2: keep titles clean; use date-only if title is blank
            formatted_date = entry_date.strftime("%A, %b %d, %Y")
            entry.title = raw_title if raw_title else formatted_date

            entry.save()
            messages.success(request, "Journal entry saved.")
            return redirect("journal:list")
    else:
        user_tz = _get_user_tz(request)
        local_now = timezone.now().astimezone(user_tz)
        form = JournalEntryForm(
            initial={
                "entry_date": local_now.replace(second=0, microsecond=0),
                "title": "",
            }
        )

    context = _build_grouped_context(request)
    context.update(
        {
            "form": form,
            "show_form": True,
        }
    )
    return render(request, "journal/journal_list.html", context)


# --------------------------------------------------
# Edit Entry
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

    context = _build_grouped_context(request)
    context.update(
        {
            "form": form,
            "show_form": True,
            "editing": True,
            "editing_entry": entry,
        }
    )
    return render(request, "journal/journal_list.html", context)


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
