"""
model.py contains the definition of the models used by the Tasks App
to define the different tasks that can be created by the users.
"""
from django.db import models
from random import randint
from .utils import random_word


class CardWithTitle(models.Model):
    """
    CardWithTitle represents a card for a feature that needs implementation,
    they provide a short title and a description.
    """
    title = models.CharField(max_length=50)

    class Meta:
        abstract = True


class IssueCard(CardWithTitle):
    """
    IssueCard represents a card for a feature that needs implementation,
    they provide a short title and a description.
    """
    description = models.CharField(max_length=500)

    def __str__(self):
        return "Issue card with Title: " + self.title + ", Description: " + self.description

    def save(self, *args, **kwargs):
        """
        save method was overwritten for this class as it will not be stored in the db
        :return: instance of the class
        """
        return self


class BugCard(CardWithTitle):
    """
    BugCard represents a card for a problem that needs fixing. It only provide a description and a title.
    The title is randomized with the following pattern: bug-{word}-{number}. It might be repeated internally.
    """
    description = models.CharField(max_length=500)

    def __str__(self):
        return "Bug card with Title: " + self.title + ", Description: " + self.description

    def save(self, *args, **kwargs):
        """
        save method was overwritten for this class as it will not be stored in the db
        :return: instance of the class
        """
        self.title = "Bug-" + random_word() + "-" + str(randint(0, 99))
        return self


class TaskCard(CardWithTitle):
    """
    TaskCard represents a card for some manual work that needs to be done.
    It counts with just a title and a category(Maintenance, Research, or Test)
    """
    CATEGORY_CHOICES = [("Maintenance", "Maintenance"),
                        ("Research", "Research"),
                        ("Test", "Test")
                        ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Maintenance")

    def __str__(self):
        return "Task card with Title: " + self.title + ", Category: " + self.category

    def save(self, *args, **kwargs):
        """
        save method was overwritten for this class as it will not be stored in the db
        :return: instance of the class
        """
        return self
