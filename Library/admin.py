from django.contrib import admin
from .models import Course, student, book, borrowing, mentor
# Register your models here.

@admin.register(Course)
class Courseadmin(admin.ModelAdmin):
    pass
    
@admin.register(student)
class studentadmin(admin.ModelAdmin):
    pass

@admin.register(book)
class bookadmin(admin.ModelAdmin):
    pass

@admin.register(borrowing)
class borrowingadmin(admin.ModelAdmin):
    pass

@admin.register(mentor)
class mentoradmin(admin.ModelAdmin):
    pass
