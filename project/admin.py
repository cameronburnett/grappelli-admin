from django.contrib import admin
from .models import Project, Site, Function, ComputeProfile, StorageProfile, SlotsOrHosts, ComputeSize, StorageTier, StorageSize, Cluster, Island
from simple_history.admin import SimpleHistoryAdmin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
import nested_admin

#register each of the models to be able to edit/add them on the admin home page. make sure to remember this 
#step if more models are added
admin.site.register(Site)
admin.site.register(Function)
admin.site.register(ComputeProfile)
admin.site.register(StorageProfile)
admin.site.register(SlotsOrHosts)
admin.site.register(ComputeSize)
admin.site.register(StorageTier)
admin.site.register(StorageSize)
admin.site.register(Cluster)
admin.site.register(Island)

#storage profile input on admin new project form
class StorageProfileInline(nested_admin.NestedTabularInline):
    #the model defines what fields should be included on the form
    model = StorageProfile

#compute profile input on admin new project form
class ComputeProfileInline(nested_admin.NestedTabularInline):
    model = ComputeProfile

#the next layer of the inline project form
class FunctionInline(nested_admin.NestedStackedInline):
    model = Function
    #models inside of function
    inlines = [StorageProfileInline, ComputeProfileInline]

#the outermost layer of the inline project form
class SiteInline(nested_admin.NestedStackedInline):
    model = Site
    #the models that live below 'site' on the new project form
    inlines = [FunctionInline]

class ProjectAdmin(nested_admin.NestedModelAdmin):
    #where admin.py connects with models.py. if you change the Project model (add a new variable, for example), 
    #that field will appear on the project form in the admin backend thanks to this line of code (model = Project)
    model = Project
    inlines = [SiteInline]
    #site header
    admin.site.site_header = 'PRNP V.1.0.0'

    #changes the structure of the admin form
    fieldsets = [
        ("Project Details", {"fields": ["project_name", "project_version", "project_class"]}),
        ("Contact Information", {"fields": ["project_contact_primary", "project_contact_secondary",]}),
    ]

    #controls which fields are displayed on the admin's list of projects
    list_display = ("project_name", "project_version", "project_class", "project_contact_primary", "project_contact_secondary", "project_created_at",)
    #allows users to filter by name, class, contact, or time of creation on the list of projects in the admin
    list_filter = ("project_name", "project_class", "project_contact_primary", "project_created_at",)
    #allows users to search for projects using the name and primary contact 
    search_fields = ("project_name", "project_contact_primary",)

    #css file to make the text boxes a bit smaller
    class Media:
        css = {
            'all': ('css/smaller_input.css',)
        }

#register the project and projectadmin form with the admin site
admin.site.register(Project, ProjectAdmin)

	

