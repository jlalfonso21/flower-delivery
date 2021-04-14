from django.contrib import admin

from socials.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_on', 'as_anon')
    list_filter = ()
    list_editable = ()
    search_fields = ()
    inlines = []
