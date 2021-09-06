from django.contrib import admin

# Register your models here.
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ("__str__")

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("__str__")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("__str__")

class LikeAdmin(admin.ModelAdmin):
    list_display = ("__str__")

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Like)