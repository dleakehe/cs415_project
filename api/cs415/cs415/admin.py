from django.contrib import admin
from .models import Characters, Classskills, Classes, Raceskills, Races, User

admin.site.register(Characters)
admin.site.register(Classskills)
admin.site.register(Classes)
admin.site.register(Raceskills)
admin.site.register(Races)
admin.site.register(User)