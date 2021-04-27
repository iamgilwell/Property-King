from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import Country, Profile
User = get_user_model()

class CountryAdmin(admin.ModelAdmin):
    list_display = ("name","available","date_added")
    list_editable=("available",)
admin.site.register(Country,CountryAdmin)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ ProfileInline]
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display =(
        'first_name','last_name','email','user_phone_number','country','role','active','staff', 'admin'
    )
    list_display_links = ('email',)
    list_selected_related = True 
    list_filter =('admin',)
    fieldsets = (
        (None, {"fields": ('email', 'password'),}),
        ('Roles', {'fields': ('role',)}), 
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'admin', 'staff', 'active')
        }),
    )

    search_fields = ('email', )
    ordering = ('email',)
    filter_horizontal = ()

    def user_phone_number(self, instance):
        return instance.profile.phone
    
    def first_name(self, instance):
        return instance.profile.first_name

    def last_name(self, instance):
        return instance.profile.last_name

    def company_name(self, instance):
        return instance.profile.company_name

    def country(self, instance):
        return instance.profile.country

admin.site.register(User, UserAdmin)