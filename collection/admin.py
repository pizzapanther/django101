from django.contrib import admin

from collection.models import Thing

@admin.register(Thing)
class ThingAdmin (admin.ModelAdmin):
    list_display = ('name', 'slug', 'Description')
    prepopulated_fields = {'slug': ('name',)}
    
    def Description (self, obj):
        return '<pre>{}</pre>'.format(obj.description)
        
    Description.allow_tags = True
    