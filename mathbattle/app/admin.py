from django.contrib import admin
from .models import Tournament

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name')
    list_display_links = ('id', 'Name')
    search_fields = ('Name', )

admin.site.register(Tournament, TournamentAdmin)

