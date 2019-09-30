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


class OrderSerializer(serializers.Serializer):

    id_show = serializers.IntegerField
    qtd_ticket = serializers.IntegerField
    id_perfil = serializers.IntegerField
    card_number = serializers.CharField
    card_name = serializers.CharField
    card_exp_month = serializers.IntegerField
    card_exp_year = serializers.IntegerField
    card_cvv = serializers.CharField

    def create(self, validated_data):
        return OrderSerializer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_show = validated_data.get('id_show', instance.id_show)
        instance.qtd_ticket = validated_data.get('qtd_ticket', instance.qtd_ticket)
        instance.id_perfil = validated_data.get('id_perfil', instance.user_code)
        instance.card_number = validated_data.get('card_number', instance.card_number)
        instance.card_name = validated_data.get('card_name', instance.card_name)
        instance.card_exp_month = validated_data.get('card_exp_month', instance.card_exp_month)
        instance.card_exp_year = validated_data.get('card_exp_year', instance.card_exp_year)
        instance.card_cvv = validated_data.get('card_cvv', instance.card_cvv)
        instance.save()
        return instance
