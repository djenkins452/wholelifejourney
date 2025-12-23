from collections import defaultdict
from zoneinfo import ZoneInfo

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import WeightEntry, Fast


@login_required
def health_index(request):
    return render(request, "health/index.html")


# ======================================================
# Weight (STABLE — DO NOT TOUCH)
# ======================================================
@login_required
def weight_list(request):
    editing_entry = None

    tz_name = request.user.profile.timezone or "UTC"
    user_tz = ZoneInfo(tz_name)

    if request.method == "POST":
        entry_id = request.POST.get("entry_id")
        weight = request.POST.get("weight")
        date = request.POST.get("date")
        note = request.POST.get("note", "")

        if not date:
            date = timezone.localtime(timezone.now(), user_tz).date()

        if entry_id:
            entry = get_object_or_404(
                WeightEntry,
                id=entry_id,
                user=request.user,
            )
            entry.weight = weight
            entry.note = note
            entry.save()

        elif weight:
            WeightEntry.objects.update_or_create(
                user=request.user,
                date=date,
                defaults={
                    "weight": weight,
                    "note": note,
                },
            )

        return redirect("health:weight_list")

    if "edit" in request.GET:
        editing_entry = get_object_or_404(
            WeightEntry,
            id=request.GET.get("edit"),
            user=request.user,
        )

    entries = WeightEntry.objects.filter(user=request.user)

    grouped = defaultdict(list)
    for entry in entries:
        week_label = entry.date.strftime("Week of %b %d")
        grouped[week_label].append(entry)

    today = timezone.localtime(timezone.now(), user_tz).date()

    return render(
        request,
        "health/weight_list.html",
        {
            "grouped_entries": dict(grouped),
            "editing_entry": editing_entry,
            "today": today,
        },
    )


@login_required
def weight_delete(request, entry_id):
    WeightEntry.objects.filter(
        id=entry_id,
        user=request.user,
    ).delete()
    return redirect("health:weight_list")


# ======================================================
# Fasting — MANUAL ENTRY (FINAL)
# ======================================================
@login_required
def fasting_list(request):
    tz_name = request.user.profile.timezone or "UTC"
    user_tz = ZoneInfo(tz_name)

    today = timezone.localtime(timezone.now(), user_tz).date()

    if request.method == "POST":
        Fast.objects.create(
            user=request.user,
            date=request.POST.get("date"),
            start_time=request.POST.get("start_time"),
            end_time=request.POST.get("end_time"),
            note=request.POST.get("note", ""),
        )
        return redirect("health:fasting_list")

    fasts = Fast.objects.filter(user=request.user)

    return render(
        request,
        "health/fasting_list.html",
        {
            "fasts": fasts,
            "today": today,
        },
    )
