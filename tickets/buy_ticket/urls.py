from django.urls import path
from .views import schedule_list, schedule_detail, buy_ticket

urlpatterns = [
    path('list/theater', schedule_list, name='schedule_list'),
    path('list/theater/<int:id>', schedule_detail, name='schedule_detail'),
    path('buy', buy_ticket, name='buy_ticket')
]
