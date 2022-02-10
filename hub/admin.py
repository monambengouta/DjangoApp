from django.contrib import admin
from .models import *
# Register your models here.
class ProjectInline(admin.TabularInline):
    model=Projet
class StudentAdmin(admin.ModelAdmin):
    list_display=(
        'last_name',
        'first_name',
        'email'
        ) # we trait how data well be display in dashboard
    fields=(
        ('last_name','first_name'), #two fields in same line
        'email' #email field has own line
    ) 
    search_fields=['last_name','email']
    inlines = [ProjectInline]
    
@admin.register(Coach) #equals to admin.site.register(Coach,CoachAdmin)
class CoachAdmin(admin.ModelAdmin):
    list_display=(
        'last_name',
        'first_name',
        'email'
        ) # we trait how data will display in dashboard
    fields=(
        ('last_name','first_name'), #two fields in same line
        'email' #email field has own line
    ) 
    search_fields=['last_name','email']

@admin.register(Projet)
class ProjectAdmin(admin.ModelAdmin):
    list_display=(
        'project_name',
        'dure',
        'description'
    )
    fieldsets=[
        (
            'state',
            {
                'fields':('isValid',)
            }
        ),
        (
            'About',
            {
               'fields':(
                'project_name',
                ('creator','supervisor'),
                'besoin',
                'description'
               )
            }
                
        ),
        (
            'Durations',
            {
                'classes': ('collapse',),
                'fields': (
                    'dure',
                    'temp_allocated'
                )
            }
        )

    ]
    #radio_fields= {'supervisor':admin.VERTICAL} radio selection button
    autocomplete_fields = ['supervisor']
    empty_value_display = '-empty-' 
    readonly_fields=['supervisor']
    
admin.site.register(Student,StudentAdmin)
admin.site.register([MemberShip])
