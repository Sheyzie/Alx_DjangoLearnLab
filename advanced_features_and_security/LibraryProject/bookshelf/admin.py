from django.contrib import admin
from .models import CustomUser, Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author')
  search_fields = ('title', 'author')
  list_filter = ('publication_year',)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )


admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)