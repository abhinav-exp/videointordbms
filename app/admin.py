from django.contrib import admin
from app.models import VideoModel, Foo
# Register your models here.

#@admin.register(Numpy)
class NAdmin(admin.ModelAdmin):
    def __str__(self) :
        return "abcdcui"


admin.site.register(VideoModel, NAdmin)

admin.site.register(Foo)

# fieldsets = (
#         (None, {'fields': ('email', 'password', 'role')}),
#         (_('Personal info'), {'fields': ('name', )}),

#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                        'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'name', 'password1', 'password2'),
#         }),
#     )
#     list_display = ('email', 'name', 'role')
#     search_fields = ('email', 'name')
#     ordering = ('email',)


