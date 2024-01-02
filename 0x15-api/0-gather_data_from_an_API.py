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
api_url = "https://jsonplaceholder.typicode.com"
response = requests.get(api_url)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse the JSON response
    todo_list = response.json()

    # Extract employee name
    name = todo_list[0]['username']

    # Count the number of completed tasks
    done_tasks = [task for task in todo_list if task['completed']]
    done_tasks = len(done_tasks)

    # Total number of tasks
    total_tasks = len(todo_list)

    # Display employee information and TODO list progress
    print(f"Employee {name} is done with tasks ({done_tasks}/{total_tasks}):")

    # Display titles of completed tasks
    for task in done_tasks:
        print(f"\t{task['title']}")

else:
    # Display an error message if the request was not successful
    print(f"Error: Unable to fetch TODO list for employee ID {employee_id}.")
    sys.exit(1)
