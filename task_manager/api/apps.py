"""
apps.py file contains the configuration setting of the API.
"""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    # TRELLO SPECIFIC SETTINGS
    # APPLICATION KEY FROM TRELLO
    API_KEY = '09145a9519682184f9cef5572c967b13'
    # TOKEN FOR THE TRELLO ADMIN USER OF THE BOARD
    API_TOKEN = '3a15f93e7b71c76c0d762c02dee38fbd6577f96e48239733207abd01a318f407'
    # DEFAULT BOARD NAME FOR THE TRELLO PROJECT
    API_DEFAULT_BOARD_NAME = 'Space-x'
    # DEFAULT LIST NAME FOR THE TRELLO PROJECT
    API_DEFAULT_LIST_NAME = 'To Do'
