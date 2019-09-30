from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import Theater, Show, Perfil, Ticket, BuyTicket
from .helpers.format_json import result_json_theater
from .helpers.credit_card import CreditCardHelper
from .helpers.status_transaction import StatusTransaction
from rest_framework.response import Response
from rest_framework import status
from mundiapi.exceptions.error_exception import *
from .helpers.serializers import OrderSerializer


@api_view(['GET'])
def schedule_list(request):
    theaters = Theater.objects.all()
    json_result = {'result': []}
    for theater in theaters:
        json_result['result'].append(result_json_theater(theater))
    return Response(json_result)


@api_view(['GET'])
def schedule_detail(request, id):
    theather = get_object_or_404(Theater, pk=id)
    json_result = result_json_theater(theather)
    return Response(json_result)


@api_view(['POST'])
def buy_ticket(request):
    data = request.data
    serializer = OrderSerializer(data=data)
    if serializer.is_valid():
        return process_tickets(data)
    else:
        return Response({'message': 'Json mal formatado'}, status=status.HTTP_400_BAD_REQUEST)


def process_tickets(data):
    show = get_object_or_404(Show, pk=data['id_show'])
    tickets = show.tickets.all().filter(show=show, is_buyer=True, is_active=True)
    aval_tickets = show.qtd_max_ticket - len(tickets)
    if data['qtd_ticket'] > aval_tickets:
        return Response({'message': 'Quantidade pedida excede a quantidade {} de ingressos disponíveis'.
                        format(aval_tickets)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return send_payment_mundipagg(data)


def send_payment_mundipagg(data):
    perfil = get_object_or_404(Perfil, pk=data['id_perfil'])
    show = get_object_or_404(Show, pk=data['id_show'])
    new_data = dict(data)
    amount = int((new_data['qtd_ticket'] * show.price * 100))
    new_data.update({'name': perfil.user.first_name, 'email': perfil.user.email,
                     'amount': amount, 'item_name': show.name})
    try:
        result = CreditCardHelper.send_invoice(new_data)
        result_status = StatusTransaction(result.status)
        if result_status is StatusTransaction.PD:
            create_tickets(new_data, perfil, show)
            return Response({'message': 'Operação concluída com sucesso'}, status=status.HTTP_200_OK)
        elif result_status is StatusTransaction.FA:
            return Response({'message': 'Operacão invalidada'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        else:
            return Response({'message': 'Código retorno desconhecido'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except ErrorException as ex:
        return Response({'message': ex.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    except Exception as ex:
        return Response({'message': ex}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def create_tickets(data, perfil, show):
    for i in range(0, data['qtd_ticket']):
        ticket = Ticket(show=show, is_buyer=True)
        ticket.save()
        buy_ticket = BuyTicket(state=StatusTransaction.PD.name, perfil=perfil, ticket=ticket)
        buy_ticket.save()
