from rest_framework import serializers
from tickets.models import Movie, Guest, Reservation

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fileds = '__all__'
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
class GuestSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('pk', 'reservation', 'name', 'mobile')



# uuid slug