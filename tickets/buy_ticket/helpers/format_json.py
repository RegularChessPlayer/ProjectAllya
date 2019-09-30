from .serializers import TheaterSerializer, ShowSerializer, TicketSerializer


def result_json_theater(theater):
    shows = theater.shows.all().filter(is_active=True)
    json_result = {'teatro': {}, 'shows': []}
    theater_serializer = TheaterSerializer(theater)
    for show in shows:
        tickets = show.tickets.all()
        show_serializer = ShowSerializer(show)
        ticket_serializer = TicketSerializer(tickets, many=True)
        json_result['shows'].append({'show': show_serializer.data,
                                     'tickets': ticket_serializer.data})
    json_result['teatro'] = theater_serializer.data
    return json_result

