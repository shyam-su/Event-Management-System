from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['user','title', 'description', 'date', 'start_time', 'end_time', 'venue', 'created_at', 'updated_at']
    list_filter = ['user', 'date','venue']
    search_fields = ['user', 'title', 'description','venue']

    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','event', 'amount', 'created_at', 'updated_at']
    list_filter = ['user', 'event']
    search_fields = ['user', 'event']
    

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['user','event', 'created_at', 'updated_at']
    list_filter =  ['user', 'event']
    search_fields = ['user', 'event']

@admin.register(EventStatus)
class EventStatusAdmin(admin.ModelAdmin):
    list_display = ['user','event', 'status', 'created_at', 'updated_at']
    list_filter =  ['user', 'event']
    search_fields = ['user', 'event']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user','event', 'rating']
    list_filter =  ['user', 'event']
    search_fields = ['user', 'event']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','event', 'text']
    list_filter =  ['user', 'event']
    search_fields = ['user', 'event']


