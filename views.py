import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from models import Musician, Album
from forms import MusicianForm, AlbumForm
from multiple_forms import *

MUSICIANS_MIN = 7

def musicians(request):
    queryset = Musician.objects.all()
    defaults = [
       {'first_name': 'Jakob', 'instrument': 'First cello'},
       {'instrument': 'Second cello'},
    ]
    if request.POST:
        posted_forms = get_posted_forms(MusicianForm, request.POST, queryset, MUSICIANS_MIN, None)
        validated_forms = validate_forms(posted_forms)
        if validated_forms:
            for form in validated_forms:
                form.save()
            return HttpResponseRedirect('/musicians')
        else:
            forms = get_posted_and_empty_forms(MusicianForm, request.POST, queryset, MUSICIANS_MIN, None)
        #TODO does not delete forms which have been emptied.
    else:
        forms = get_db_forms(MusicianForm, queryset, defaults, MUSICIANS_MIN)

    forms = set_fields_to_readonly(forms, defaults)

    context = {
        'forms': forms
    }
    return render_to_response('musicians.html', context)



