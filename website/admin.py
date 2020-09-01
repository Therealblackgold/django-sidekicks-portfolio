from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.site_header = 'Sidekicks Online'


admin.site.register(Post)