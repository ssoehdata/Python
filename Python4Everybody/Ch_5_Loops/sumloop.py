zork = 0
print("Before", zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + thing
    print(zork, thing)
print("After", zork)

# adding a members in a set to orig variable value 
# successively in a loop

# performs and prints additional math operations as well
count = 0
sum = 0
print("Before",count, sum)
for value  in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum / count)


