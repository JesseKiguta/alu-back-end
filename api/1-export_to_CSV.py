#!/usr/bin/python3


"""
Retrieve and print information about an employee's tasks.

Args:
employee_id (int): The employee ID.

Prints:
Employee progress information for each task in the following format:
'USERID','USERNAME','TASK_COMPLETED_STATUS','TASK_TITLE'
"""

import csv
import requests
import sys

if __name__ == "__main__":

    """
    Gets the employee ID

    Puts the links of APIs into variables

    Retrieves data from the API and parses the data

    Exports the data in the CSV format
    """

    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command line argument
    employee_id = sys.argv[1]

    # Define the API endpoints for todos and users
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    # Send HTTP GET requests to retrieve data from the API
    todo_response = requests.get(todo_url)
    user_response = requests.get(user_url)

    # Create a CSV filename based on the employee ID
    csv_filename = f'{employee_id}.csv'

    # Open the CSV file for writing
    with open(csv_filename, 'w', newline='') as csv_file:
	# Create a CSV writer object
        csv_writer = csv.writer(csv_file)
	# Write the CSV header
    	csv_writer.writerow(["USER_ID", "USERNAME",
			"TASK_COMPLETED_STATUS", "TASK_TITLE"])

    # Iterate through the todo items
    for todo in todo_data:
	# Gets the employees data to be printed
	if todo.get('userId') == employee_id:
		# Matches the user to their employee ID
		user = next((user for user in user_data if
			user['id'] == employee_id), None)
                if user:
		    # Writes task details to the CSV file
                    employee_name = user['name']
                    task_completed = "completed" if todo['completed']
					else "not completed"
                    task_title = todo['title']
                    csv_writer.writerow([employee_id, employee_name,
					task_completed, task_title])
    # Confirm data is saved
    print(f"Data saved to {csv_filename}")
