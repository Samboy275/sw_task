![alt text](https://rightshero.com/wp/wp-content/uploads/2024/04/RightsHero-Logo.png)

# Samual's Software Engineer Task Project
This is my implementation of the given task using Django
There are 2 ways to run the project locally


## [1] Using Docker-Compose
To run the project in this setting the provided .env file must be in the same directory as the docker-compose.yaml file then run the following command:

```
docker-compose up
```

**make sure you have the following files before running the command**

- .env
- requirements.txt

Now you can access the project at [http://0.0.0.0:8000](http://0.0.0.0:8000)

## [2] Without Using Docker
  **make sure there is no environment variables for database in the .env file to run the project using this method**

This will run the Django project using the `sqlite3` database with the following commands:

- First, create a virtual environment

```bash
python -m venv ./venv
```

- Then, activate the virtual environment

  - On **Linux/macOS**:

  ```bash
  source venv/bin/activate
  ```

  - On **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- Install the required dependencies

```bash
pip install -r requirements.txt
```

- Apply migrations to the database

```bash
python manage.py migrate
```

- Finally, run the Django development server

```bash
python manage.py runserver
```
To use `mysql` instead of `sqlite3`, follow these steps:

1. Install MySQL on your machine.
2. Create a database for the application.
3. Create a user and grant them the necessary privileges.

Then, add the following credentials to your `.env` file:

- `MYSQL_USER`: **The database user you just created**
- `MYSQL_DATABASE`: **The name of the database**
- `MYSQL_PASSWORD`: **The password for the user**
- `MYSQL_HOST`: **The host where MySQL is running (e.g., `localhost`)**
- `MYSQL_PORT`: **The port MySQL is listening on (default is `3306`)**


Now, you can access the project at [http://127.0.0.1:8000](http://127.0.0.1:8000)



# Notes

- Its not good practice to push .env files that hold environment variables and important secrets into a repo but this is a task so it is an exception.
