from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile,Moo

admin.site.unregister(Group)

class profileMove(admin.StackedInline):
    model = Profile
    
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [profileMove]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Moo)
