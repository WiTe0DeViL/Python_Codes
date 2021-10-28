# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space
# between them

first_name = input("Enter the First Name : ")
last_name = input("Enter the Last Name : ")

print(last_name[::-1] + " " + first_name[::-1])
