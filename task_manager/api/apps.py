"""
apps.py file contains the configuration setting of the API.
"""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    # TRELLO SPECIFIC SETTINGS
    # APPLICATION KEY FROM TRELLO
    API_KEY = 'Set your API_KEY here'
    # TOKEN FOR THE TRELLO ADMIN USER OF THE BOARD
    API_TOKEN = 'Set your API_TOKEN here'
    # DEFAULT BOARD NAME FOR THE TRELLO PROJECT
    API_DEFAULT_BOARD_NAME = 'Space-x'
    # DEFAULT LIST NAME FOR THE TRELLO PROJECT
    API_DEFAULT_LIST_NAME = 'To Do'
