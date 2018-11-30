# File: django.py
from listprops import ListProps

class Doc(ListProps):
    """
    To start a new Django project, first create a python virtual environment:
        $ python3 -m venv <env_name>

    Activate the virtual environment:
        $ cd <env_name>
        $ . bin/activate

    Next, install Django via pip:
        (<env_name>) $ pip install django

    Create a new Django project:
        (<env_name>) $ django-admin startproject <project_name>

    Create a new Django app in project:
        (<env_name>) $ cd <project_name>
        (<env_name>) $ python3 manage.py startapp <app_name> 

    """
