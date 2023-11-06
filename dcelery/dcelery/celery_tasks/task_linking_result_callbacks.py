from ..celery_config import app

@app.task(queue='tasks')
def main_task():
    # Your main task code here
    raise ValueError('Something went wrong.')
    result = "Main task executed successfully"
    return result

@app.task(queue='tasks')
def follow_up_task1(result_from_main):
    # Your follow-up task 1 code here
    result = f"Follow-up task 1 executed with result: {result_from_main}"
    return result

@app.task(queue='tasks')
def follow_up_task2(result_from_follow_up1):
    # Your follow-up task 2 code here
    result = f"Follow-up task 2 executed with result: {result_from_follow_up1}"
    return result

@app.task(queue='tasks')
def error_handler(exc, task_id, args):
    # Handle the error and take appropriate action
    error_message = f"An error occurred in task {task_id}: {str(exc)}"
    print(error_message)
    # Log the error, send notifications, or perform other error handling tasks

def run_tasks():
    main_task.apply_async(link=[follow_up_task1.s(), follow_up_task2.s()], link_error=[error_handler.s(),])
