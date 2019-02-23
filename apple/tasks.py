from celery.decorators import task


@task(name="add_numbers")
def add_numbers(a, b):
    return a + b
