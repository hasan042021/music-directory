from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        widgets = {
            "rating": forms.RadioSelect(),
            "release_date": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M", attrs={type: "datetime-local"}
            ),
        }
