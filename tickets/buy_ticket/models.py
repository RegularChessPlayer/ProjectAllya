from django.db import models
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
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    price = models.FloatField('Preço Ingresso')

    def __str__(self):
        return self.name


class User(models.Model):

    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):

    code = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    is_active = models.BooleanField('Ticket Válido', default=True)

    def __str__(self):
        return self.code


class BuyTicket(models.Model):

    state = models.CharField(max_length=5, choices=[(status.name, status.value) for status in StatusTransaction])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return 'Cod: {} - {}'.format(self.state, self.ticket.code)
