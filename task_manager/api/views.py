from .serializers import IssueCardSerializer, BugCardSerializer, TaskCardSerializer
from rest_framework.views import APIView, Response, status
from .trello_utils import create_card


class CreateCardView(APIView):
    """
    TaskManagerApi defines the api endpoint for creating tasks in Trello.
    """
    def post(self, request):
        """
        post method will receive a post request from the client, identify the card type to be created, validate its data
        and send the correct request to Trello API using trello_utils methods.
        :param request: post request from the client
        :return: Response object with an status code and the url to the created card or an error message if something
        fails.
        """
        # Determines card type
        if 'type' in request.data:
            card_type = request.data['type']
        else:
            card_type = None
        # Process Issue Card creation request
        if card_type == 'issue':
            card_serializer = IssueCardSerializer(data=request.data)
            if card_serializer.is_valid():
                card = card_serializer.save()
                response_data = create_card(card)
            else:
                response_data = {"error": card_serializer.errors}
        # Process Bug Card creation request
        elif card_type == 'bug':
            card_serializer = BugCardSerializer(data=request.data)
            if card_serializer.is_valid():
                card = card_serializer.save()
                response_data = create_card(card, "Bug", True)
            else:
                response_data = {"error": card_serializer.errors}
        # Process Task Card creation request
        elif card_type == 'task':
            card_serializer = TaskCardSerializer(data=request.data)
            if card_serializer.is_valid():
                card = card_serializer.save()
                response_data = create_card(card, card.category)
            else:
                response_data = {"error": card_serializer.errors}
        # Process not existent card type creation request
        else:
            response_data = {"error": 'Wrong card type!'}
        # Validates response to send correct status to the client
        if "error" in response_data:
            response_status = status.HTTP_400_BAD_REQUEST
        else:
            response_status = status.HTTP_201_CREATED
        return Response(data=response_data, status=response_status)
