from django.contrib import admin
# to make model visible on Admin page register with admin.site.register(Post)
from .models import Post


admin.site.register(Post)
