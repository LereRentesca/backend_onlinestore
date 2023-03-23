#working with list

#create a list
ages=[]

#add elements to a list
ages.append(38)
ages.append(34)
ages.append(32)
ages.append(48)
ages.append(58)

#for cycles
for x in ages:
    print(x)


#getting total age
total_sum=0;
for x in ages:
    total_sum += x
print(total_sum)