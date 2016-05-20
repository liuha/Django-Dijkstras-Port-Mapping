from django.contrib import admin

# Register your models here.
from .models import NetworkPort, Edge, Node

admin.site.register(NetworkPort)
admin.site.register(Node)
admin.site.register(Edge)
