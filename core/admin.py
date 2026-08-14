from django.contrib import admin
from .models import (
    ContactMessage,
    SiteSettings,
    Project,
    ProjectImage,
    ProjectComment,
    ProjectLike
)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectCommentInline(admin.TabularInline):
    model = ProjectComment
    extra = 0
    fields = ('name', 'email', 'message', 'admin_reply', 'is_approved', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    can_delete = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'client_name',
        'project_location',
        'status',
        'featured',
        'is_published',
        'display_order',
        'created_at',
    )
    list_filter = (
        'category',
        'status',
        'featured',
        'is_published',
        'created_at',
    )
    search_fields = (
        'title',
        'short_description',
        'description',
        'client_name',
        'project_location',
        'overview',
        'scope',
        'technologies',
        'tags',
    )
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('featured', 'is_published', 'display_order')
    inlines = [ProjectImageInline, ProjectCommentInline]

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'title',
                'slug',
                'category',
                'short_description',
                'description',
                'overview',
                'image',
            )
        }),
        ('Client / Project Details', {
            'fields': (
                'client_name',
                'project_location',
                'contract_value',
                'start_date',
                'completion_date',
                'duration',
                'floors',
                'total_area',
                'status',
            )
        }),
        ('Project Content', {
            'fields': (
                'scope',
                'technologies',
                'tags',
            )
        }),
        ('Challenge & Solution', {
            'fields': (
                'challenge_1_title',
                'challenge_1_desc',
                'solution_1_title',
                'solution_1_desc',
            )
        }),
        ('Publishing', {
            'fields': (
                'featured',
                'is_published',
                'display_order',
            )
        }),
    )


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption')
    search_fields = ('project__title', 'caption')


@admin.register(ProjectComment)
class ProjectCommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'project',
        'is_approved',
        'created_at',
    )
    list_filter = ('is_approved', 'created_at', 'project')
    search_fields = ('name', 'email', 'message', 'admin_reply', 'project__title')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Comment Info', {
            'fields': ('project', 'name', 'email', 'message', 'created_at')
        }),
        ('Admin Reply / Moderation', {
            'fields': ('admin_reply', 'is_approved')
        }),
    )


@admin.register(ProjectLike)
class ProjectLikeAdmin(admin.ModelAdmin):
    list_display = ('project', 'ip_address', 'created_at')
    list_filter = ('created_at', 'project')
    search_fields = ('project__title', 'ip_address')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'service', 'created_at')
    list_filter = ('service', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'message', 'company', 'location')
    readonly_fields = ('created_at',)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone_1', 'phone_2')