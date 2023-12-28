from invoke import task

@task
def mk(c):
    c.run("python manage.py makemigrations")

@task
def mi(c):
    c.run("python manage.py migrate")

@task
def run(c):
    c.run("python manage.py runserver")