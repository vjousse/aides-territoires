from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from aids.models import Aid
from aids.forms import AidAdminForm


class AidAdmin(admin.ModelAdmin):
    """Admin module for aids."""

    form = AidAdminForm
    fieldsets = [
        (None, {
            'fields': (
                'name',
                'description',
                'author',
                'backer',
                'status',
            )
        }),

        (_('Aid description'), {
            'fields': (
                'is_funding',
                'aid_types',
                'aid_types_detail',
                'destinations',
                'destinations_detail',
                'thematics',
                'subvention_rate',
                'keywords',

            )
        }),

        (_('Eligibility'), {
            'fields': (
                'eligibility',
                'application_perimeter',
                'mobilization_steps',
                'targeted_audiances',
                'targeted_audiances_detail',
                'minimal_population',
                'maximal_population',
            )
        }),

        (_('Contact'), {
            'fields': (
                'url',
                'contact_email',
                'contact_phone',
                'contact_detail'
            )
        }),


        (_('Calendar'), {
            'fields': (
                'publication_status',
                'start_date',
                'predeposit_date',
                'submission_deadline',
            )
        })
    ]


admin.site.register(Aid, AidAdmin)