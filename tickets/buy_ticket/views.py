from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import Theater
from .helpers.format_json import result_json_theater
from rest_framework.response import Response


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
    pass
