# try and except example

# Write a program to prompt the user for hours and rate per hour
# using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 
# times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input 
# - assume the user types numbers properly. 


sh = input('Enter hours: ')
sr = input("Enter rate: ")
try: 
    fh = float(sh)
    fr = float(sr)
except:
    print("Error.Please enter numeric input.")
    quit()

print(fh, fr)
if fh > 40:
    # print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)    
    xp = reg + otp 
else:     
    xp = fh * fr
print(f"Pay:", xp)

 
