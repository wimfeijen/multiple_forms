from django import forms

from models import Musician, Album

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician 
        # multiple_forms loops over these fields, so they have to be specified.
        fields = [
            'first_name',
            'last_name',
            'instrument',
        ]

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album 
        # multiple_forms loops over these fields, so they have to be specified.
        fields = [
            'artist',
            'name',
            'release_date',
            'num_stars',
        ]

