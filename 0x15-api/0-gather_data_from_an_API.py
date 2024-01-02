#!/usr/bin/python3
"""
using API to gather employee data
"""

import re
import requests
import sys

# Ensure that an employee ID is provided as a command line argument
if len(sys.argv) != 2:
    print("Usage: python script.py <employee_id>")
    sys.exit(1)

# Extract the employee ID from the command line argument
employee_id = int(sys.argv[1])

# API endpoint URL
api_url = "https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
response = requests.get(api_url)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse the JSON response
    todo_list = response.json()
    if todo_list:
        # Extract employee name
        name = todo_list[0]['username']

        # Count the number of completed tasks
        done_tasks = [task for task in todo_list if task['completed']]
        num_tasks = len(done_tasks)

        # Total number of tasks
        total = len(todo_list)

        # Display employee information and TODO list progress
        print(f"Employee {name} is done with tasks ({num_tasks}/{total}):")

        # Display titles of completed tasks
        for task in done_tasks:
            print(f"\t{task['title']}")
    else:
        print(f"No TODO list found for employee ID {employee_id}")

else:
    # Display an error message if the request was not successful
    print(f"Error: Unable to fetch TODO list for employee ID {employee_id}.")
    sys.exit(1)
