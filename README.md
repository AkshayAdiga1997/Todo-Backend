# Todo-Backend

Simple Todo backend application which uses flask and mysql. Allows to create/modify and delete todos.

## Prerequisites

-   Python 3.6 (Installed through anaconda)
-   Anaconda 4.5.11
    -   Mac
        -   [Download](https://www.anaconda.com/download/#macos)
        -   Install the dmg file.
-   MySQL 5.7
    -   Mac
        -   _brew install mysql@5.7_

## Setting up

-   Create a database and table with the following character set and collation.
    -   Refer src/database/
-   Clone the repository.
-   Create the virtual environment using anaconda.
    -   _conda create -n todo python=3.6_
-   Activate the anaconda virtual environment.
    -   _conda activate todo_
-   Install all the required packages in your virtual environment.
    -   _pip install -r requirements.txt_
-   Update the database values in _etc/config/secrets.ini_.
-   Run Flask server (inside src directory) with
    -   _python app.py_
-   Access the APIs with.
    -   _localhost:5000/fetch_todo_
    -   _localhost:5000/add_todo_
