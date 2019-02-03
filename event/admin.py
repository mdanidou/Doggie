from django.contrib import admin
from .models import Dog_Event, Category, Judge, Club, Dog


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)

class JudgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'country']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Judge, JudgeAdmin)

class ClubAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'country', 'address']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Club, ClubAdmin)

class DogAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Dog, DogAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'slug', 'image', 'description', 'judge', 'club', 'dog','price', 'date']
    list_filter = ['category', 'date', 'dog']
    list_editable = ['description', 'price']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Dog_Event,EventAdmin)

