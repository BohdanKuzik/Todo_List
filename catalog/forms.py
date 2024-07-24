from django import forms


class TaskSearchForm(forms.Form):
    content = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by content"}),
    )
