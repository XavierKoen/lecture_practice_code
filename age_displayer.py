"""
User prompted to input age and is told whether odd or even.
Error checks in play as well.
"""
finished = False

while not finished:
    try:
        user_age = int(input("Please enter age: "))
        while user_age < 0:
            user_age = int(input("Error! Invalid age! Please enter a positive integer: "))
        finished = True
    except ValueError:
        print("Error! Invalid age! Positive integer required.")

odd_test = user_age % 2
if odd_test:
    result = "odd"
else:
    result = "even"
print("Your age is {}.".format(result))
