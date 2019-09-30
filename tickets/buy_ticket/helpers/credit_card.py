from mundiapi.mundiapi_client import MundiapiClient
from mundiapi.models import *
from mundiapi.controllers import *

SUCESSO = '4000000000000010'
FALHA = '4000000000000028'
PROCESSING = '4000000000000036'

class CreditCardHelper:

    MundiapiClient.config.basic_auth_user_name = "sk_test_jGEYM24HQ2HgzxwN:"
    orders_controller = orders_controller.OrdersController()

    @classmethod
    def send_invoice(cls, data):
        customer = create_customer_request.CreateCustomerRequest()
        customer.name = data['name']
        customer.email = 'tony_stak@gmail.com'

        credit_card = create_credit_card_payment_request.CreateCreditCardPaymentRequest()
        credit_card.capture = True
        credit_card.installments = 2
        credit_card.statement_descriptor = "test descriptor"
        credit_card.card = create_card_request.CreateCardRequest()
        credit_card.card.number = data['card_number']
        credit_card.card.holder_name = data['card_name']
        credit_card.card.exp_month = data['card_exp_month']
        credit_card.card.exp_year = data['card_exp_year']
        credit_card.card.cvv = data['card_cvv']

        request = create_order_request.CreateOrderRequest()

        request.items = [create_order_item_request.CreateOrderItemRequest()]
        request.items[0].description = data['item_name']
        request.items[0].quantity = data['qtd_ticket']
        request.items[0].amount = data['amount']

        request.payments = [create_payment_request.CreatePaymentRequest()]
        request.payments[0].payment_method = "credit_card"
        request.payments[0].credit_card = credit_card
        request.customer = customer
        return cls.orders_controller.create_order(request)
