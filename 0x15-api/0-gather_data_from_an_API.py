#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/"
    user = requests.get(link + f"users/{sys.argv[1]}").json()
    todos = requests.get(link + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print(f"\t {c}") for c in completed]
