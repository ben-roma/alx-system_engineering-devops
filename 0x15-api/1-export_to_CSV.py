#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    try:
        user = requests.get(f"{url}users/{user_id}").json()
        username = user.get("username")
        todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

        with open(f"{user_id}.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for t in todos:
                writer.writerow([user_id, username, t.get("completed"),
                                 t.get("title")])

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
