#1. Write a Python script to take user input and store it in a list
user_list = []
def GetByUser_string(value):
    value = input(f"Enter {value} ")
    return value


def GetByUser_int(value):
    value = int(input(f"Enter {value} "))
    return value
user_list.append(GetByUser_string("Name"))
user_list.append(GetByUser_int("age"))
print(user_list)