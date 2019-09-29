from django.db import models
from django.contrib.auth.models import User
from .helpers.status_transaction import StatusTransaction
import uuid


class Theater(models.Model):

    name = models.CharField(max_length=50)
    qtd_max = models.IntegerField()

    def __str__(self):
        return self.name


class Show(models.Model):

    name = models.CharField(max_length=50)
    date_show = models.DateField()
    is_active = models.BooleanField('Show Ativo', default=True)
    theater = models.ForeignKey(Theater, related_name='shows', on_delete=models.CASCADE)
    price = models.FloatField('Preço Ingresso')
    qtd_max_ticket = models.IntegerField('Quantidade disponível ingressos', default=100)

    def __str__(self):
        return self.name


class Perfil(models.Model):

    user = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.user.username


class Ticket(models.Model):

    code = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    show = models.ForeignKey(Show, related_name='tickets', on_delete=models.CASCADE)
    is_active = models.BooleanField('Ticket Válido', default=True)
    is_buyer = models.BooleanField('Ticket Comprado', default=False)

    def __str__(self):
        return self.code


class BuyTicket(models.Model):

    state = models.CharField(max_length=5, choices=[(status.name, status.value) for status in StatusTransaction])
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='buy_ticket')

    def __str__(self):
        return 'Cod: {} - {}'.format(self.state, self.ticket.code)
