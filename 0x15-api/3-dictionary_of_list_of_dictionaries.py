#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    try:
        users = requests.get(f"{url}users").json()
        todos = requests.get(f"{url}todos").json()

        all_tasks = {}

        for u in users:
            user_id = u.get("id")
            username = u.get("username")
            user_tasks = [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos if t.get("userId") == user_id]

            all_tasks[user_id] = user_tasks

        with open("todo_all_employees.json", "w") as jsonfile:
            json.dump(all_tasks, jsonfile)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
