from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from backend.forms import CustomUserCreationForm, CustomUserChangeForm

from backend.models import Category, AdminUser, CustomerUser, Product

from django.utils.html import format_html
from django.db.models import Q

# Register your models here.
class BaseCustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'gender', 'image_tag', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        # (None, {'fields': ('first_name', 'last_name', 'email', 'gender', 'password', 'groups')}),
        ('Basic Information', {'fields': ('first_name', 'last_name', 'gender','password')}),
        ('Contact Information', {'fields': ('email',)}),
        ('Permissions', {'fields': ('groups', 'is_staff', 'is_active')}),
    )

    add_fieldsets = (
        # (None, {
        #     'classes': ('wide',),
        #     'fields': ('first_name', 'last_name', 'email', 'gender', 'password1', 'password2', 'is_staff', 'is_active', 'groups')}
        #  ),
        ('Basic Information', {'fields': ('first_name', 'last_name', 'gender','password1','password2')}),
        ('Contact Information', {'fields': ('email',)}),
        ('Permissions', {'fields': ('groups', 'is_staff', 'is_active')}),
    )

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

# Filter users by group or role (adjust logic if using roles instead of groups)
@admin.register(CustomerUser)
class CustomerAdmin(BaseCustomUserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(groups__name='Customer')


@admin.register(AdminUser)
class AdminUserAdmin(BaseCustomUserAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(
            Q(groups__name='Admin') | Q(groups=None)
        )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','price','image_tag',)

    def image_tag(self, obj):
        return format_html('<img src = "{}" width = "150" height="150" />'.format(obj.image_path.url))

    image_tag.short_description = 'Image'