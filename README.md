# task_scheduler_celery_django

# Celery Scheduler Project

This project demonstrates how to use Celery with Django to schedule tasks and perform asynchronous processing, specifically for sending emails to all users in the database.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/scheduler-project.git
cd scheduler-project
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source  "venv\Scripts\activate"
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Configure Django settings:

Ensure that you have a `scheduler_project/settings.py` file with the necessary database and email settings. Also, make sure to set `CELERY_BROKER_URL` and `CELERY_RESULT_BACKEND` in the settings.

5. Run Celery worker:

Open a terminal and run the following command to start the Celery worker:

```bash
celery -A scheduler_project worker --loglevel=info
```

6. Run Celery beat:

Open another terminal and run the following command to start Celery beat, responsible for scheduling tasks:

```bash
celery -A scheduler_project beat --loglevel=info
```

7. Start Django development server:

In a new terminal, run the following command to start the Django development server:

```bash
python manage.py runserver
```

## Usage

Once everything is set up, you can access the following endpoints:

- `/test`: This endpoint triggers a test task to check if Celery is working correctly. When accessed, it will asynchronously execute the `test_func` task.

- `/send_mail_to_all`: This endpoint triggers the `send_mail_func` task, which sends an email to all users in the database. The emails will be sent based on the schedule defined in Celery Beat settings (`app.conf.beat_schedule`).

## Understanding Celery Settings

In the `scheduler_project/celery.py` file, you can find the Celery configuration and task definitions. Here's a brief explanation of the important parts:

- Celery App: The `app` object is the main Celery application instance, and it is created with the name "scheduler_project".

- Timezone: The timezone for task scheduling is set to 'Asia/Kolkata' to match the Indian Standard Time (IST).

- Celery Beat: Celery Beat is used to schedule tasks. In the `app.conf.beat_schedule`, we define the schedule for the `send_mail_func` task. It is set to run every day at 16:10 (4:10 PM).

- Task Definitions: The `send_mail_func` task is defined using the `@shared_task` decorator. This task sends emails to all users in the database using Django's built-in `send_mail` function.

## Contributing

If you find any issues or want to contribute to this project, feel free to create a pull request or open an issue.

We hope this project helps you understand how to use Celery with Django for scheduling tasks and performing asynchronous processing. If you have any questions or need further assistance, don't hesitate to reach out! Happy coding!
