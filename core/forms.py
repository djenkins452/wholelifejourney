from django import forms
from zoneinfo import available_timezones
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    timezone = forms.ChoiceField(
        choices=[(tz, tz) for tz in sorted(available_timezones())],
        label="Time Zone"
    )

    display_name = forms.CharField(
        label="Display Name",
        max_length=100,
        required=False,
        help_text="How your name appears in the app"
    )

    class Meta:
        model = UserProfile
        fields = ["display_name", "timezone"]
