#search using a boolean var
# here we search for a specific value (3)
found = False
print('Before', found)
for value in [9,41,12,3,74,15]:
    if value == 3: 
        found = True
    print(found, value)
print('After', found)