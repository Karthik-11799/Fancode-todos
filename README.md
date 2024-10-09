# FanCode SDET Assignment
## Overview
This project is an API automation task where we verify that all users from the city "FanCode" have completed more than 50% of their "todo" tasks. The city "FanCode" is identified based on specific latitude and longitude values retrieved from the users' data.
### Scenario:
- **Given**: A user has todo tasks.
- **And**: The user belongs to the city FanCode.
- **Then**: The user's completed task percentage should be greater than 50%.
### FanCode City Identification:
- Latitude between `-40` and `5`.
- Longitude between `5` and `100`.
The project interacts with the following APIs from [jsonplaceholder](https://jsonplaceholder.typicode.com/):
- `/users`: Retrieves all users.
- `/todos`: Retrieves all tasks for specific users.

