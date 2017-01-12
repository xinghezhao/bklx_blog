from django.contrib import admin
from .models import Catagory, Tag, Blog, Achievement, Person, Speak,Skill,Life,Aboutme

# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','created')

class SpeakAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')

class AboutmeAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'birthday')

admin.site.register(Catagory)
admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Achievement)
admin.site.register(Person)
admin.site.register(Speak,SpeakAdmin)
admin.site.register(Skill)
admin.site.register(Life)
admin.site.register(Aboutme)