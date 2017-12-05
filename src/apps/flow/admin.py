from django.contrib import admin
from fsm_admin.mixins import FSMTransitionMixin

from .models import Order, State, StateTransition


class OrderModelAdmin(FSMTransitionMixin, admin.ModelAdmin):
    fsm_field = ['state', ]
    search_fields = ('awb',)
    list_display = (
        'awb',
        'state',
    )
    list_filter = (
        'state',
    )
    readonly_fields = (
        'state',
    )


admin.site.register(Order, OrderModelAdmin)
admin.site.register(State)
admin.site.register(StateTransition)
