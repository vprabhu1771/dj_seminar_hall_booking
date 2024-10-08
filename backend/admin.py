from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from backend.models import CustomUser, Venue, Booking

from django.contrib.auth.admin import UserAdmin
from backend.forms import CustomerUserCreationForm,CustomerUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomerUserCreationForm
    form = CustomerUserChangeForm
    model = CustomUser
    list_display = ('email','gender','image_tag','is_staff','is_active',)
    list_filter = ('email','is_staff','is_active',)
    fieldsets = (
        (None,{'fields': ('email','gender','password')}),
        ('Permissions',{'fields':('is_staff','is_active', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','gender','password1','password2','is_staff','is_active', 'groups', 'user_permissions')}
         ),
    )

    search_fields = ('email',)

    ordering = ('email',)

    def image_tag(self,obj):
        return format_html('<img src = "{}"width="150" height="150"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

admin.site.register(CustomUser,CustomUserAdmin)

class VenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity', 'image_tag',)

    def image_tag(self,obj):
        return format_html('<img src = "{}"width="150" height="150"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

admin.site.register(Venue, VenueAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'event_type',
        'venue',
        'capacity',
        'event_date',
        'event_starting_time',
        'event_ending_time',
        'organizer'
    )

admin.site.register(Booking, BookingAdmin)