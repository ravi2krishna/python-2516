# Client Program To Get number of users records -> 30
# Client Program To Filter Users based on age less than 30 and give usernames
import json
with open("lms.json","r") as file_data:
    data = json.load(file_data)
    for user in data['users']:
        if user['age'] < 30:
            print(user['username'], user['age'])
# print(data)
# print(type(data))
# print("Total Users: ",len(data['users']))

