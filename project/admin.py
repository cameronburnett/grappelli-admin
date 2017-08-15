from django.contrib import admin
from .models import Project, Site, Function, ComputeProfile, StorageProfile, SlotsOrHosts, ComputeSize, StorageTier, StorageSize, Cluster, Island
from simple_history.admin import SimpleHistoryAdmin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
import nested_admin

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

class StorageProfileInline(nested_admin.NestedTabularInline):
    model = StorageProfile

class ComputeProfileInline(nested_admin.NestedTabularInline):
    model = ComputeProfile

class FunctionInline(nested_admin.NestedStackedInline):
    model = Function
    inlines = [StorageProfileInline, ComputeProfileInline]

class SiteInline(nested_admin.NestedStackedInline):
    model = Site
    inlines = [FunctionInline]

#@admin.register(Project)
class ProjectAdmin(nested_admin.NestedModelAdmin):
    change_list_filter_template = "admin/filter_listing.html"
    model = Project
    inlines = [SiteInline]
    admin.site.site_header = 'PRNP V.1.0.0'

    fieldsets = [
        ("Project Details", {"fields": ["project_name", "project_version", "project_class"]}),
        ("Contact Information", {"fields": ["project_contact_primary", "project_contact_secondary",]}),
    ]

    list_display = ("project_name", "project_version", "project_class", "project_contact_primary", "project_contact_secondary", "project_created_at",)

    list_filter = ("project_name", "project_class", "project_contact_primary", "project_created_at",)
    search_fields = ("project_name", "project_contact_primary",)
    #inlines = [ComputeProfileInline, StorageProfileInline]

    class Media:

        css = {
            'all': ('css/smaller_input.css',)
        }

admin.site.register(Project, ProjectAdmin)

	

