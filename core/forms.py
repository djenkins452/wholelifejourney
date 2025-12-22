from django import forms
from zoneinfo import available_timezones
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    timezone = forms.ChoiceField(
        choices=[(tz, tz) for tz in sorted(available_timezones())],
        label="Time Zone"
    )

    class Meta:
        model = UserProfile
        fields = ["timezone"]
