#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])  # Convert user_id to integer
    url = "https://jsonplaceholder.typicode.com/"

    try:
        user = requests.get(f"{url}users/{user_id}").json()
        username = user.get("username")
        todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

        tasks = [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]

        with open(f"{user_id}.json", "w") as jsonfile:
            json.dump({user_id: tasks}, jsonfile)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
