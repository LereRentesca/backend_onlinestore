from about import me

for key, value in me.items():
    print(key,' : ',value)

me["age"] += 1
print(me)

me["color"]="green"
print(me)

#HW1
print(f'{me["name"]} : {me["age"]}')

#HW2
me.pop("age")
print(me)
