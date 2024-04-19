from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import *

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item)
admin.site.register(Movie_search)
admin.site.register(Result)
admin.site.register(Category)
admin.site.register(Profile)