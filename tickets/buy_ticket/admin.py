from django.contrib import admin
from .models import Theater, Show, Perfil, Ticket, BuyTicket

MODELS = [Theater, Show, Perfil, Ticket, BuyTicket]

admin.site.register(MODELS)
