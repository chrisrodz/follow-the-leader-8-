from django.contrib import admin
from ccomforms.models import T02, A125, T02Form

class T02Admin(admin.ModelAdmin):
	form = T02Form
	readonly_fields = T02._meta.get_all_field_names()

admin.site.register(T02, T02Admin)
admin.site.register(A125)