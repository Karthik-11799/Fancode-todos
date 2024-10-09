import pytest
from src.api_service import get_users, get_todos_by_user
from src.business_logic import is_user_in_fancode_city, calculate_completed_percentage
@pytest.fixture
def users():
   return get_users()
def test_users_from_fancode(users):
   """Test that all users from FanCode city have >50% tasks completed."""
   for user in users:
       if is_user_in_fancode_city(user):
           todos = get_todos_by_user(user['id'])
           completion_percentage = calculate_completed_percentage(todos)
           assert completion_percentage > 50, f"User {user['id']} has less than 50% tasks completed"
