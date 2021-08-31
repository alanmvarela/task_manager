# Introduction
A Task Manager for the space-x program Trello board. This Task Manager is a Rest API that accepts post request to create different types of cards into an existent Trello board.

# Installation
1. Create virtual env.
2. Clone repository into virtual env directory.
3. Install requirements from requirements.txt by:
- Navigate to the root directory of the project. Should be something like "~/task_manager"
- Activate the virtual env.
- Run: $ pip install -requirements.txt
4. Create db migrations by:
- Navigate to the main directory of the project. Should be something like "~/task_manager/task_manager"
- Run: $ python manage.py migrate
5. Set API configuration settings:
 - Navigate to the api app directory. Should be something like "~/task_manager/api"
 - Modify configuration settings under TRELLO SPECIFIC SETTINGS section in the apps.py file.
    * API_KEY: it's the Api key obtained from the administrator of the trello account that will be used for this project.
    * API_TOKEN: it's the token obtained from the API_KEY previously created.
    * API_DEFAULT_BOARD_NAME: it's the name of the Trello board where the cards creation requested to the API will be created.
    * API_DEFAULT_LIST_NAME: it's the name of the Trello list where the cards creation requested to the API will be created.
6. Set preconditions on Trello:
- Login in the Trello account from where you got the API_KEY value.
- Create a Board with API_DEFAULT_BOARD_NAME name.
- Create a List in the previously created board with API_DEFAULT_LIST_NAME name.
- Create labels 'Bug', 'Maintenance', 'Research' and 'Test' in the previously created board.
7- Run the API unit test to see that everything is working fine:
- Navigate to the main directory of the project. Should be something like "~/task_manager/task_manager"
- Activate the virtual env.
- Run: $ python manage.py test
8. Start the API:
- Navigate to the main directory of the project. Should be something like "~/task_manager/task_manager"
- Activate the virtual env.
- Run: $ python manage.py runserver
- Access the api endpoint in your browser using the url http://127.0.0.1:8000/
- Fill the content with an accepted format like for e.g: {"type": "task", "category": "Maintenance", "title": "a title"} and send the request to see it working! 
 
 
 # Design Assumptions and Notes
 - As the list to be assigned to hasn't been specified neither for Bug or Task cards they will be assigned to the "To Do" List.
 - As there's no specification about if the task cards should be assigned to an user or not, they will not be assigned to any user.
 - The created API don't need to handle the creation of neither the board, lists or labels that will be used by the Space-x project.
 - The unit test of the API will only work if the preconditions are met and should only be run with API_DEFAULT_BOARD_NAME setting pointing to 
  a Test board that has to be previously created manually.
