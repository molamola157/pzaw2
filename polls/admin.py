from django.contrib import admin
from .models import Post
from .models import Vote
from .models import CustomUser
# Register your models here.

admin.site.register(Post)
admin.site.register(Vote)
admin.site.register(CustomUser)