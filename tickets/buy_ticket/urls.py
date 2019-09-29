from django.urls import path
from .views import schedule_list, schedule_detail

urlpatterns = [
    path('list/theater', schedule_list, name='schedule_list'),
    path('list/theater/<int:id>', schedule_detail, name='schedule_detail')
]
