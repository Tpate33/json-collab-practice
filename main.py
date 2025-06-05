import json

# task 1 (load json file):
x = open("practice.json")
data = json.load(x)
x.close()

# task 2 (Print all message id):
print("Task 2:")
for i in data:
    print(i["messageID"])
print()

# task 3 : Print User Authentication Methods (userID and authentication)
print("Task 3:")
for i in data:
    print("UserID: ", i['userInfo']['userID'])
    print("Authetication Method: ", i['userInfo']['authentication']['method'])
    print()


