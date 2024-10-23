from rest_framework import serializers
from .models import *


class EventSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = Event
        fields = ('__all__')
        
        
class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = Payment
        fields = ('__all__')
        
        
class AttendanceSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = Attendance
        fields = ('__all__')
        
        
class EventStatusSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = EventStatus
        fields = ('__all__')
        
        
class RatingSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = Rating
        fields = ('__all__')
        
        
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = Comment
        fields = ('__all__')