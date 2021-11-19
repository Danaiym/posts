from django.contrib import admin
from .models import Post, Hashtag, Image

admin.site.register(Post)
admin.site.register(Hashtag)
admin.site.register(Image)
