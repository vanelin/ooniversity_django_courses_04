# -*- coding: utf-8 -*-
from django.contrib import admin
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):

    '''
        Admin View for CoachAdmin
    '''
    list_display = ('name', 'last_name', 'gender', 'skype', 'description')
    list_filter = ('user__is_staff',)

admin.site.register(Coach, CoachAdmin)
