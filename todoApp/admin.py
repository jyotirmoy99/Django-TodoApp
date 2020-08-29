from django.contrib import admin
from .models import Todo


class TodAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Todo, TodAdmin)
