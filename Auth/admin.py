from django.contrib import admin
from .models import Document,Notification,Access
# Register your models here.
admin.site.register(Document)
admin.site.register(Notification)
admin.site.register(Access)