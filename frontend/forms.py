from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from backend.models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(BookingForm, self).__init__(*args, **kwargs)

        self.fields['event_type'].widget.attrs.update({'class': 'form-control'})

        self.fields['venue'].widget.attrs.update({'class': 'form-control'})

        self.fields['capacity'].widget.attrs.update({'class': 'form-control'})

        self.fields['event_date'].widget.attrs.update({'class': 'form-control'})

        self.fields['event_starting_time'].widget.attrs.update({'class': 'form-control'})

        self.fields['event_ending_time'].widget.attrs.update({'class': 'form-control'})

        self.fields['organizer'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        fields = '__all__'
        model = Booking
        widgets = {
            'event_date': DateInput,
            'event_starting_time': TimeInput,
            'event_ending_time': TimeInput
        }
