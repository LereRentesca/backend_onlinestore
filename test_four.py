
def users():
    people = [
        {'name':'Alice',  'age':25},
        {'name':'Bob',    'age':30},
        {'name':'Charlie','age':35},
        {'name':'Dave',   'age':40},
        {'name':'Emily',  'age':45}
    ]
    sum_ages=0;

    for user in people:
        print(user)

    for user in people:
        print(user["name"])
    
    for user in people:
        if user["age"]>30:
            print(f'Name: {user["name"]} -- Age: {user["age"]}')

    for user in people:
        sum_ages += user["age"]
    print(f'Total Ages: {sum_ages}')    

    name = str(input("Type the user name:"))
    flag = True
    for user in people:
        if user["name"].lower()==name.lower():
            print(f'Name: {name} => Age: {user["age"]}')
            flag = False
    if flag:
        print("User doesn't exist")
    

def print_total():
    print("your total is: 123")

def can_drink(age):
    if age < 19:
        print("You can't drink!")
    else:
        print("You can drink")

# print_total()
# can_drink(22)
users()