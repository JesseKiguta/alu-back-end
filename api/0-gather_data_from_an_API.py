#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command line argument
    employee_id = sys.argv[1]

    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    todo_response = requests.get(todo_url)
    user_response = requests.get(user_url)

    todo_data = todo_response.json()
    user_data = user_response.json()

    if 'name' in user_data:
        name = user_data['name']

    completed_tasks = [task for task in todo_data if task['userId'] == int(employee_id) and task['completed']]
    total_tasks = [task for task in todo_data if task['userId'] == int(employee_id)]

    print(f"Employee {name} is done with tasks({len(completed_tasks)}/{len(total_tasks)}):")
    for task in completed_tasks:
        print("\t " + task['title'])