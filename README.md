# Meeting Planner - Django Sample Project

Course link - [Django: Getting Started
](https://app.pluralsight.com/library/courses/django-getting-started/table-of-contents)

## Steps to run the code

Start with creating virtual env (have to do it only once)

`` virtualenv -p `which python3.9` .venv ``

Activate the created venv (have to do every time you want to run code from bash/cli)

`source .venv/bin/activate`

More one time thing to install requirements -

`pip install -r requirements.txt`

`pip freeze > requirements.txt`

Migrate the DB for one time and at each time after fresh changes to schema

`python manage.py migrate`

And, Finally to run server

`python manage.py runserver`

you will be getting something like this on console

```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 29, 2021 - 15:48:21
Django version 3.0.2, using settings 'meeting_planner.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Code will be running on - [http://127.0.0.1:8000](http://127.0.0.1:8000/)
