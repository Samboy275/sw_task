![alt text](https://rightshero.com/wp/wp-content/uploads/2024/04/RightsHero-Logo.png)


# Software Engineer Task Assessment

This role will be part of the Rightshero software development team.

As a software engineer you are a part of a small but very efficient and multi-tasking team.

The team is tasked with handling all the software aspects of our service.

# The task
The task will be a **project** and **AWS CloudFormation** template:

## [1] The project:
A project contains one page have a 2 categories checkboxes

- [ ] Category A
- [ ] Category B

Unlimited subcategories of parent category (if it is hard to achieve the unlimited levels, you can set 3 levels hard-coded)
Should use Ajax.

### Example
- [ ] Category A
- [ ] Category B

If user select “Category B”
The system will create another 2 checkboxes with

- [ ] SUB Category B1
- [ ] SUB Category B2

Selecting Sub Category B2 will create another 2 checkboxes

- [ ] SUB SUB Category B2-1
- [ ] SUB SUB Category B2-2
 And so on


## [2] AWS CloudFormation
An AWS CloudFormation template YAML file for:
- Launch a t2.micro or t3.micro EC2 instance
- Create IAM role with admin privileges
- Attach the IAM role to the EC2 instance created earlier
- Deploy the project on the EC2 instance
- The instance should be accessable via SSH, HTTP and HTTPS protocols/ports


# Notes
- We would be scoring for the below aspects of the assignment:
- DB,Architecture /Code (preferred MVC pattern), Security, Git
- You could use a framework to create the project from scratch (Django).
- You should use MySQL or Postgresql Databases.
- Please use one table design in the database for all categories and subs.
- The code should contain comments with important information.
- README file for run the project locally.
- The **AWS CloudFormation** template file.


# Deliverables
- The project should be ready with docker compose (web service + DB).
- The **AWS CloudFormation** template YAML file.
- Once you're finished, submit a PR to this repo with your email in a commit message.
- The email should be the same as your email in the CV/Resume.


# Samual's Software Engineer Task Project
This is my implementation of the given task using Django
There are 2 ways to run the project locally


## [1] Using Docker-Compose
To run the project in this setting the provided .env file must be in the same directory as the docker-compose.yaml file then run the following commands:

- First the database service DB
```bash
docker-compose up DB
```

- Once its running use another terminal to run the web service **note that the DB service must show that it is ready for connection before running this command**
```bash
docker-composer up --build web_service
```
Now you can access the project at [http://0.0.0.0:8000](http://0.0.0.0:8000)

## [2] Without Using Docker

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

Now, you can access the project at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

