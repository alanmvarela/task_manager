"""
trello_utils contains all the methods used for the communication with
trello api.
"""
import requests
import json
from api import apps
from random import randint


def create_card(card, label=None, assigned=False, board_name=apps.ApiConfig.API_DEFAULT_BOARD_NAME):
    """
    create_card creates a new card on a Trello board
    :param card: the card instance to be created in Trello.
    :param label: the label name to be assigned to the created card. If None no label will ne assigned
    :param assigned: flag to indicate if the created card should be assigned to a random member of the board.
    False by default.
    :param board_name: the name of the board to where the card should be created. API_DEFAULT_BOARD_NAME by default.
    :return: url to the created card or error message associated to the request.
    """
    # Recover Trello id of the board where the card will be created
    board_id = get_board_id(board_name)
    # Validates if there's any issues recovering the board id
    if "error" in board_id:
        return board_id
    # Recover Trello id of the list where the card will be created
    list_id = get_list_id(apps.ApiConfig.API_DEFAULT_LIST_NAME, board_id)
    # Validate if there's any issues recovering the list id
    if "error" in list_id:
        return list_id
    # Defines the base Trello API url for creating the new card
    creation_url = 'https://api.trello.com/1/cards?key=' + apps.ApiConfig.API_KEY \
                   + '&token=' + apps.ApiConfig.API_TOKEN \
                   + '&name=' + card.title \
                   + '&idList=' + list_id
    # Validates if the new card should have a Trello label
    if label is not None:
        # Recover the id of the label to be assigned to the new card
        label_id = get_label_id(label, board_id)
        # Validates if there's any issues recovering the label id
        if "error" in label_id:
            return label_id
        # Adds the label id to the Trello API url
        creation_url += '&idLabels=' + label_id
    # Validates if the new card should be assigned to a member of the Trello Board
    if assigned:
        # Recover the id of a random user to assign the new card to
        member_id = get_random_member_id(board_id)
        # Validates if there's any issues recovering the user id
        if "error" in member_id:
            return member_id
        else:
            # Adds the user id to the Trello API url
            creation_url += '&idMembers=' + member_id
    try:
        # Tries to add the new card description to the Trello API url
        creation_url += '&description=' + card.description
    except AttributeError:
        # The current card has no description
        pass
    # Sends request to Trello API and returns a response to the client
    return send_post_request(creation_url)


def get_board_id(board_name):
    """
    :param board_name: The name of the Trello board to get the id for.
    :return: The id of the Trello board passed as parameter, error is there is any problem with the request
    or None if the board does not exist in Trello.
    """
    board_id = None
    response = requests.get('https://api.trello.com/1/members/me/boards?key=' + apps.ApiConfig.API_KEY
                            + '&token=' + apps.ApiConfig.API_TOKEN)
    if response.ok:
        content = json.loads(response.content)
        for i in content:
            if i["name"] == board_name:
                board_id = i["id"]
                break
    else:
        return {"error": str(response.status_code) + " returned while trying to recover '"
                + board_name + "' board from Trello"}
    if board_id is None:
        return {"error": "The board '" + board_name + "' does not exist in Trello"}
    else:
        return board_id


def get_list_id(list_name, board_id):
    """
    :param list_name: name of the list to recover the Trello id from.
    :param board_id: Trello id for the board where the list will be look for.
    :return: the Trello id of the list passed as parameter, error is there is any problem with the request
    or None if the list Trello id is not found.
    """
    list_id = None
    response = requests.get('https://api.trello.com/1/boards/' + board_id
                            + '/lists?key=' + apps.ApiConfig.API_KEY
                            + '&token=' + apps.ApiConfig.API_TOKEN)
    if response.ok:
        content = json.loads(response.content)
        for i in content:
            if i["name"] == list_name:
                list_id = i["id"]
                break
    else:
        return {"error": str(response.status_code) + " returned while trying to recover '"
                + list_name + "' list from Trello"}
    if list_id is None:
        return {"error": "The list '" + list_name + "' does not exist in Trello board with id: '" + board_id + "'"}
    else:
        return list_id


def get_label_id(label_name, board_id):
    """
    :param label_name: name of the label to recover the Trello id from.
    :param board_id: Trello id for the board where the label will be look for.
    :return: the Trello id of the list passed as parameter, error is there is any problem with the request
    or None if the label Trello id is not found.
    """
    label_id = None
    response = requests.get('https://api.trello.com/1/boards/' + board_id
                            + '/labels?key=' + apps.ApiConfig.API_KEY
                            + '&token=' + apps.ApiConfig.API_TOKEN)
    if response.ok:
        content = json.loads(response.content)
        for i in content:
            if i["name"] == label_name:
                label_id = i["id"]
                break
    else:
        return {"error": str(response.status_code) + " returned while trying to recover '"
                + label_name + "' label from Trello"}
    if label_id is None:
        return {"error": "The label '" + label_name + "' does not exist in Trello board with id: '" + board_id + "'"}
    else:
        return label_id


def get_random_member_id(board_id):
    """
    :param board_id: Trello id for the board where the label will be look for.
    :return: the Trello id of a random member of the board or error if no Trello member id is recovered.
    """
    response = requests.get('https://api.trello.com/1/boards/' + board_id
                            + '/members?key=' + apps.ApiConfig.API_KEY
                            + '&token=' + apps.ApiConfig.API_TOKEN)
    if response.ok:
        content = json.loads(response.content)
        member_id = content[randint(0, len(content)-1)]["id"]
    else:
        return {"error": str(response.status_code) + " returned while trying to recover users list from Trello board"}
    return member_id


def create_board(board_name):
    """
    create_board method creates a new board in Trello
    :param board_name: name of the board to be created
    :return: url to the created board or error message associated to the response
    """
    creation_url = 'https://api.trello.com/1/boards?key=' + apps.ApiConfig.API_KEY \
                   + '&token=' + apps.ApiConfig.API_TOKEN \
                   + '&name=' + board_name
    return send_post_request(creation_url)


def create_list(list_name, board_id):
    """
    create_list creates a new list in an existent Trello board
    :param list_name: name of the list to be created
    :param board_id: id of the Trello board where the list will be created
    :return: url to the created list or error message associated to the response
    """
    creation_url = 'https://api.trello.com/1/lists?key=' + apps.ApiConfig.API_KEY \
                   + '&token=' + apps.ApiConfig.API_TOKEN \
                   + '&name=' + list_name \
                   + "&boardId=" + board_id
    return send_post_request(creation_url)


def create_label(label_name, board_id):
    """
    create_label creates a new label in an existent Trello board
    :param label_name: name of the label to be created
    :param board_id: id of the Trello board where the label will be created
    :return: url to the created label or error message associated to the response.
    """
    creation_url = 'https://api.trello.com/1/labels?key=' + apps.ApiConfig.API_KEY \
                   + '&token=' + apps.ApiConfig.API_TOKEN \
                   + '&name=' + label_name \
                   + '&color=' + '' \
                   + "&boardId=" + board_id
    return send_post_request(creation_url)


def send_post_request(url):
    """
    send_post_request sends a post request to the Trello API and returns its response
    :param url: Trello API url to where the post request should be sent
    :return: url associated to the response or the response itself if there is any error.
    """
    response = requests.post(url)
    if response.ok:
        content = json.loads(response.content)
        return {"message": content["url"]}
    else:
        return {"error": response}
