#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]

    try:
        user = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}")
        user.raise_for_status()
        name = user.json().get('name')

        todos = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
        todos.raise_for_status()
        todos_data = todos.json()

        total_tasks = len(todos_data)
        completed_tasks = [
            task for task in todos_data if task.get('completed')
        ]

        print(f'Employee {name} is done with tasks({len(completed_tasks)}/'
              f'{total_tasks}):')
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
