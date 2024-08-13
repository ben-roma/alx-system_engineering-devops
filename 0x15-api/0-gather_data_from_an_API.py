#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    """Fetches and displays the TODO list progress for a given employee."""
    
    # URL de base de l'API
    base_url = "https://jsonplaceholder.typicode.com/"
    
    # Récupération des informations de l'employé
    user_url = f"{base_url}users/{employee_id}"
    response_user = requests.get(user_url)
    if response_user.status_code != 200:
        print("Employee not found.")
        return
    
    user_data = response_user.json()
    employee_name = user_data.get("name")
    
    # Récupération des tâches de l'employé
    todos_url = f"{base_url}todos?userId={employee_id}"
    response_todos = requests.get(todos_url)
    todos_data = response_todos.json()
    
    # Filtrage des tâches complétées
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)
    
    # Affichage des résultats
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
