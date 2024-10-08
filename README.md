# Fancode-todos
Assessment 
Project Overview
The Todo Automation project automates the process of checking whether users from the fictional city "FanCode" have more than 50% of their todo tasks completed. It utilizes the JSONPlaceholder API, which provides sample data for users and their todo tasks.

Project Structure
Directory Structure:
tests/: Contains unit tests to verify the functionality of the main script.
requirements.txt: Lists the dependencies required to run the project.
README.md: Provides documentation and instructions for setting up and using the project.
main.py: Contains the main logic for fetching user data, calculating completion percentages, and checking if users meet the criteria.

Key Components
API Interaction:

The project interacts with the JSONPlaceholder API, specifically using endpoints to get user data and todo tasks.
Endpoints Used:
/users: To retrieve user information.
/todos: To retrieve todo tasks associated with each user.
Geographical Filtering:

The project defines "FanCode" city based on geographical coordinates. A user is considered part of "FanCode" if:
Latitude is between -40 and 5.
Longitude is between 5 and 100.
Completion Percentage Calculation:

For each user identified as being from "FanCode":
The script retrieves their todo tasks.
It calculates the percentage of completed tasks by counting how many tasks are marked as completed versus the total number of tasks.
Results Evaluation:

The script checks if the completion percentage for each user is greater than 50%.
It stores the results and can print or log them for review.
Implementation Steps
Fetching Users:

The get_users() function makes a GET request to the /users endpoint and retrieves a list of users.
Filtering Users by Location:

The is_in_fancode_city() function checks if a user’s latitude and longitude fall within the specified range.
Fetching Todo Tasks:

The get_todos(user_id) function retrieves the todo tasks for each user based on their user ID.
Calculating Completion:

The calculate_completion_percentage(todos) function calculates the percentage of completed tasks. It sums up completed tasks and divides by the total tasks to get the percentage.
Main Functionality:

The check_fancode_users_completion() function orchestrates the process:
It fetches all users.
Filters them to find those from "FanCode".
For each of these users, it retrieves their todo tasks and checks their completion percentage.
The results are stored in a dictionary where the keys are user names and values indicate if their completion percentage is greater than 50%.
Testing
The tests/test_todos.py file contains unit tests that utilize the unittest framework to verify the correctness of the check_fancode_users_completion() function.
The tests assert that all users from "FanCode" have more than 50% of their todo tasks completed.
Conclusion
This project showcases how to use APIs, filter data based on specific criteria, perform calculations, and implement testing for functionality. It emphasizes good coding practices like modularization, code reusability, and structuring, making it maintainable and easy to understand. The project can be extended or modified further based on additional requirements or functionalities.
