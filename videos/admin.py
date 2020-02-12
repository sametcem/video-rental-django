from django.contrib import admin

# Register your models here.
from . import models


class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year', 'title', 'length'] #Gorunme siralari

    search_fields = ['title','length'] #Search based title

    list_filter = ['release_year', 'length' , 'title']


    list_display = [ 'title','release_year', 'length' ]

    list_editable = ['length']
admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)