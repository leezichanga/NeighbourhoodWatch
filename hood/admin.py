from django.contrib import admin
from .models import MyUser,Post,Business,Neighborhood

# Register your models here.
admin.site.register(Post)
admin.site.register(MyUser)
admin.site.register(Business)
admin.site.register(Neighborhood)
