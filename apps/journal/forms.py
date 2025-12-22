from django import forms
from .models import JournalEntry


class JournalEntryForm(forms.ModelForm):
    entry_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local"
            }
        ),
        label="Entry Date"
    )

    class Meta:
        model = JournalEntry
        fields = ["title", "entry_date", "body"]
        labels = {
            "title": "",   # 👈 remove label so placeholder acts as label
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Enter Title Here",
                    "style": "width: 100%;",
                }
            ),
            "body": forms.Textarea(
                attrs={
                    "placeholder": "Start Your Journal Entry Here",
                    "style": "width: 100%;",
                    "rows": 8,
                }
            ),
        }
