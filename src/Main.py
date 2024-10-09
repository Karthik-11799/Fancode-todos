from src.api_service import get_users, get_todos_by_user
from src.business_logic import is_user_in_fancode_city, calculate_completed_percentage
def main():
   users = get_users()
   for user in users:
       if is_user_in_fancode_city(user):
           todos = get_todos_by_user(user['id'])
           completion_percentage = calculate_completed_percentage(todos)
           if completion_percentage > 50:
               print(f"User {user['name']} has more than 50% tasks completed.")
           else:
               print(f"User {user['name']} has less than 50% tasks completed.")
if __name__ == "__main__":
   main()
