from django.contrib import admin

from .models import Bb, Rubric, AdvUser, Machine, Spare


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')
    search_help_text = 'Enter text for search'


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
admin.site.register(AdvUser)
admin.site.register(Machine)
admin.site.register(Spare)
