

from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined')

class BootAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class NetworkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class StorageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ComputeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class UXAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class FeedbackAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class WorkflowAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Site)
admin.site.register(User, UserAdmin)
admin.site.register(Boot, BootAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Compute, ComputeAdmin)
admin.site.register(UX, UXAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Workflow, WorkflowAdmin)

