from django.contrib import admin
from .models import Course, Attandance, UnitGroup, Sokongan, UserProfile


admin.site.register(Course)
admin.site.register(Attandance)
admin.site.register(UnitGroup)
admin.site.register(Sokongan)
admin.site.register(UserProfile)

# Register your models here.
