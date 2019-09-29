from rest_framework import serializers
from buy_ticket.models import Theater, Show, Ticket


class TheaterSerializer(serializers.ModelSerializer):

    class Meta:

        model = Theater
        fields = '__all__'


class ShowSerializer(serializers.ModelSerializer):

    class Meta:

        model = Show
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):

    class Meta:

        model = Ticket
        fields = '__all__'
