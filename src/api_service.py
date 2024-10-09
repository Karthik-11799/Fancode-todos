import requests
BASE_URL = "http://jsonplaceholder.typicode.com"
def get_users():
   """Fetch all users."""
   response = requests.get(f"{BASE_URL}/users")
   response.raise_for_status()
   return response.json()
def get_todos_by_user(user_id):
   """Fetch todos for a specific user."""
   response = requests.get(f"{BASE_URL}/todos", params={"userId": user_id})
   response.raise_for_status()
   return response.json()
