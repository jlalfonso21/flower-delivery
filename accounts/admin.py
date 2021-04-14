from django.contrib import admin

# Register your models here.
from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mun',)
    list_filter = ()
    list_editable = ()
    search_fields = ()
    inlines = []
