"""alphabet = input("alphabet: ")

if(alphabet in "aeiouAEIOU"):
    print("alphabet is a vowel")

else:
    print("alphabet is consolant")"""

'''
exp = input("Data for eval: ")
result = eval(exp)
print(f"The output is {result}")

'''
'''

correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful! Welcome,", username)
else:
    print("Login failed! Invalid username or password.")


'''
'''
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a + b > c and a + c > b and b + c > a:
    print("The triangle is valid.")
else:
    print("The triangle is NOT valid.")
'''


a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))


if a + b > c and a + c > b and b + c > a:
    #
    if a == b == c:
        print("Triangle type: Equilateral")
    elif a == b or b == c or a == c:
        print("Triangle type: Isosceles")
    else:
        print("Triangle type: Scalene")
else:
    print("Not a valid triangle")
