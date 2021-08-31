"""
test_api.py file contains the unit test for the api calls.
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ApiCreateCardUnitTest(APITestCase):
    """
    The ApiCreateTaskUnitTest class includes all the test related to the api.
    """
    def test_create_issue_card(self):
        """
        test_create_issue_card validates that a issue card can be created
        successfully in an existent list that's part of a Trello board.
        """
        url = reverse('api:create_card')
        data = {"type": "issue", "description": "a description", "title": "a title"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg=response.content.decode("utf-8"))

    def test_create_bug_card(self):
        """
        test_create_bug_card validates that a bug card can be created
        successfully with a label in an existent list that's part of a Trello board.
        """
        url = reverse('api:create_card')
        data = {"type": "bug", "description": "a description"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg=response.content.decode("utf-8"))

    def test_create_task_card(self):
        """
        test_create_task_card validates that an task card can be created
        successfully with a label in an existent list that's part of a Trello board.
        """
        url = reverse('api:create_card')
        data = {"type": "task", "category": "Maintenance", "title": "a title"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg=response.content.decode("utf-8"))

