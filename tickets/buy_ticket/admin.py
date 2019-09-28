from django.contrib import admin
from .models import Theater, Show, User, Ticket, BuyTicket

MODELS = [Theater, Show, User, Ticket, BuyTicket]

admin.site.register(MODELS)

