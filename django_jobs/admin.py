from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Job


class JobAdminMixin(object):

    fields = (
        'is_enabled',
        'get_handler_name',
        'extra_status',
        'status',
        'error_message',
        'created',
        'modified',
    )

    readonly_fields = (
        'get_handler_name',
        'error_message',
        'content_type',
        'object_id',
        'modified',
        'created',
        'status',
    )

    def get_handler_name(self, obj):
        return obj.maker_object.get_handler_name(obj.handler_id)

    get_handler_name.short_description = 'handler'


class JobTabularInline(JobAdminMixin, GenericTabularInline):
    model = Job
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    extra = 0

    def has_add_permission(self, request):
        return False


@admin.register(Job)
class JobAdmin(JobAdminMixin, admin.ModelAdmin):
    list_display = (
        'maker_object',
        'get_handler_name',
        'extra_status',
        'status',
        'error_message',
        'is_enabled',
        'created',
        'modified',
    )

    list_filter = (
        'is_enabled',
        'extra_status',
        'status',
    )
