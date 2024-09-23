from django.contrib import admin

from zuzenketak.models import Exercise, Student, Submission

# Register your models here.

admin.site.register(Exercise)
admin.site.register(Student)
admin.site.register(Submission)