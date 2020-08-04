from django.contrib import admin

from .models import Payment

# from django.contrib.sessions.models import Session
# session_key = request.data['sessionKey']
# session = Session.objects.get(session_key=session_key)
# Session.objects.filter(session_key=session).delete()
# Session.objects.all().delete()

# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if request.user.is_superuser:
#             obj.is_staff = True
#             obj.save()

admin.site.register(Payment)
