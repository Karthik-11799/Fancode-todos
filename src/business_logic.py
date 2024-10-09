def is_user_in_fancode_city(user):
   """Check if the user belongs to FanCode city."""
   lat = float(user['address']['geo']['lat'])
   lng = float(user['address']['geo']['lng'])
   return -40 <= lat <= 5 and 5 <= lng <= 100
def calculate_completed_percentage(todos):
   """Calculate percentage of completed todos."""
   total_tasks = len(todos)
   if total_tasks == 0:
       return 0  # Avoid division by zero if there are no tasks
   completed_tasks = sum(1 for todo in todos if todo['completed'])
   return (completed_tasks / total_tasks) * 100
