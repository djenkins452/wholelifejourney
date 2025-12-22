from django import forms
from .models import JournalEntry


class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(attrs={
                "rows": 10,
                "placeholder": "Write your thoughts here..."
            })
        }
