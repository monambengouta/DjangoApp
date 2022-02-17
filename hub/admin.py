from random import sample
from django.contrib import admin,messages
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
        'email' #email field in one line
    ) 
    search_fields=['last_name','email']
    inlines = [ProjectInline]
    
class ProjectDurationFilter(admin.SimpleListFilter):
    parameter_name="duration"
    title="dure"
    def lookups(self, request, model_admin): #A lookup is a query expression with a left-hand side
        return (
            ('1 Month','less than 1 month'),
            ('3 Months','less than 3 months'),
            ('More','Other')
        )
    def queryset(self, request, queryset): #Returns a new QuerySet containing objects that match the given lookup parameters. 
        if self.value() == "1 Month":
            return queryset.filter(dure__lte=30)
        elif self.value() == "3 Months":
            return queryset.filter(dure__lte=90,dure__gt=30)#exclude() is a reverse off filter
        elif self.value()=="More": return queryset.filter(dure__gt=90)




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

def set_Valid(modeladmin,request,queryset):
    rows=queryset.update(isValid=True) #exécuter une requete sur la table pour faire une update
    if rows == 1:
        msg="1 project was"
    else: 
        msg= f"{rows} projcts were"
    messages.success(request, message=f"{msg} successfully markes is valid")
set_Valid.short_description = "Validate project" #action description





@admin.register(Projet)
class ProjectAdmin(admin.ModelAdmin):
    
    actions=[set_Valid,'set_InValid'] # 'set_InValid ' cuz the methode is inside class 
    actions_on_bottom=True  
    list_filter=(
        'creator','isValid',ProjectDurationFilter
    )
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
    
    def set_InValid(modeladmin,request,queryset):
        
        rows=queryset.update(isValid=False) #exécuter une requete sur la table pour faire une update
        if rows == 1:
            msg="1 project was "
        else: 
            msg= f"{rows} projcts were "
        messages.success(request, message=f"{msg} successfully markes is Invalid")


    
admin.site.register(Student,StudentAdmin)
admin.site.register([MemberShip])
