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

#task 4: Task 4: Total the Payment Amount
payment_amount = 0
for sessions in data:
    payment_amount += sessions['userInfo']['payment']['amount']
print("This is the total payment amount across all sessions " + str(payment_amount))
print('\n')

#Task 5: Filter Sessions by Payment Method
for sessions in data:
    if(sessions['userInfo']['payment']['method'] == 'credit_card'):
        print(sessions)
