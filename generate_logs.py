# Phase 3A - Random Log Generator
# Task 1 - Set Up the Script
import json
import random
import uuid
import datetime


# Task 2 - Build a Template for One Session
randomDict = {}
vendorList = ["ChargeGrid", "GreenCharge", "VoltNet"]

# Generate random userID
randomInt = random.randint(10000, 99999)
intStr = str(randomInt)
randomDict['UserID'] = "user-" + intStr

# Random selects vendor
vendorIndex = random.randint(0, len(vendorList)-1)
randomDict['Vendor'] = vendorList[vendorIndex]

# Random generate startTime and endTime
# start_time = ""
# weekDays = "SMTWTFS"
# year = random.randint(1907, 2025)
# month = random.randint(1,12)
# # need to check leap year how many days in the month for days
# day = 
# #weekDays[random.randint(0, len(weekDays))]
# start_time = year + '-' month 


# Random generate cost and method
method = ["credit_card", "mobile_wallet"]
randomDict['Amount'] = round(random.uniform(5.00, 30.00), 2)
methodIndex = random.randint(0, len(method) - 1)
randomDict["Method"] = method[methodIndex]


# Random generate authentication method + token
methodAut = ["RFID", "app_login", "app_qr"]
randomDict["Authentication"] = methodAut[random.randint(0, len(methodAut) - 1)]

# Token
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXZ"
randToken = ""

while (len(randToken) != 8) :
    tokenNum = random.randint(0, 1)
    # 0 for alphabet
    if (tokenNum == 0):
        randToken = randToken + alpha[random.randint(0, len(alpha)-1)]
    # 1 for digits 0-9
    else:
        randToken = randToken + str(random.randint(0,9))

randToken = randToken[:4] + '-' + randToken[4:]
randomDict["Token"] = randToken

# Random messageID
msgID = random.randint(0, 999)
if (msgID < 100):
    if (msgID < 10):
        msgStrID = "00" + str(msgID)
    else:
        msgStrID = "0" + str(msgID)

else:
    msgStrID = str(msgID)
msgStr = "msg-20250605-" + msgStrID
randomDict["MessageID"] = msgStr

# print(randomDict)


# Task 3 - Generate N Random Sessions

session_list = []
for i in range(0,99):
    # everything below was copied from task 2
    randomDict = {}
    vendorList = ["ChargeGrid", "GreenCharge", "VoltNet"]

    # Generate random userID
    randomInt = random.randint(10000, 99999)
    intStr = str(randomInt)
    randomDict['UserID'] = "user-" + intStr

    # Random selects vendor
    vendorIndex = random.randint(0, len(vendorList)-1)
    randomDict['Vendor'] = vendorList[vendorIndex]

    # Random generate startTime and endTime
    # start_time = ""
    # weekDays = "SMTWTFS"
    # year = random.randint(1907, 2025)
    # month = random.randint(1,12)
    # # need to check leap year how many days in the month for days
    # day = 
    # #weekDays[random.randint(0, len(weekDays))]
    # start_time = year + '-' month 


    # Random generate cost and method
    method = ["credit_card", "mobile_wallet"]
    randomDict['Amount'] = round(random.uniform(5.00, 30.00), 2)
    methodIndex = random.randint(0, len(method) - 1)
    randomDict["Method"] = method[methodIndex]


    # Random generate authentication method + token
    methodAut = ["RFID", "app_login", "app_qr"]
    randomDict["Authentication"] = methodAut[random.randint(0, len(methodAut) - 1)]

    # Token
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXZ"
    randToken = ""

    while (len(randToken) != 8) :
        tokenNum = random.randint(0, 1)
        # 0 for alphabet
        if (tokenNum == 0):
            randToken = randToken + alpha[random.randint(0, len(alpha)-1)]
        # 1 for digits 0-9
        else:
            randToken = randToken + str(random.randint(0,9))

    randToken = randToken[:4] + '-' + randToken[4:]
    randomDict["Token"] = randToken

    # Random messageID
    msgID = random.randint(0, 999)
    if (msgID < 100):
        if (msgID < 10):
            msgStrID = "00" + str(msgID)
        else:
            msgStrID = "0" + str(msgID)

    else:
        msgStrID = str(msgID)
    msgStr = "msg-20250605-" + msgStrID
    randomDict["MessageID"] = msgStr
    session_list.append(randomDict)

print(session_list)


# Task 4 - Export to random_sessions.json
random_session = json.dumps(session_list, indent = 4)
w = open("random_sessions.json", "w")
w.write(random_session)
w.close()
print()