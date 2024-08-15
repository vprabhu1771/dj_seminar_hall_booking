from django.db.models import Q
from django.shortcuts import render

from backend.models import Venue, Booking
from frontend.forms import BookingForm


# Create your views here.
def home(request):
    global is_booked
    if request.method == 'POST':
        form = BookingForm(request.POST)
        #print(request.POST['venue'])

        if form.is_valid():

            # Printing Data
            #print(form.cleaned_data)

            #print(form.cleaned_data.get('event_type'))

            #print(form.cleaned_data.get('venue'))

            venue = Venue.objects.get(name=form.cleaned_data.get('venue'))

            bookings = Booking.objects.filter(
                Q(venue=form.cleaned_data.get('venue')) & Q(event_date__exact=form.cleaned_data.get('event_date'))
            ).first()
            is_booked = False
            print(bookings)
            if bookings:
                print("Venue Already Booked")
            else:
                is_booked = True
                form.save()
            context = {
                'form': BookingForm(None),
                'is_booked': is_booked
            }
            return render(request, "frontend/home.html", context)
        else:
            context = {
                'form': form
            }
            #print(form.errors)
            return render(request, "frontend/home.html", context)

    context = {
        'form': BookingForm(None),
        'is_booked': None
    }

    return render(request, "frontend/home.html",context)