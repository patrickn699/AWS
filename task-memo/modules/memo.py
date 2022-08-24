import boto3
import datetime



def create_memo(task_name, task_description, task_status, task_priority, task_due_date, task_created_date, task_updated_date):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('task-memo-table')

    table.put_item(
        Item={
            'task_name': task_name,
            'task_description': task_description,
            'task_status': task_status,
            'task_priority': task_priority,
            'task_due_date': task_due_date,
            'task_created_date': task_created_date,
            'task_updated_date': task_updated_date
        }
    )
    return 'successfully inserted', task_due_date