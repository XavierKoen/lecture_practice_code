question = input("I'm thinking of a number between 1 and 10, what is it? ")
ANSWER = '7'
print(question)
while question != ANSWER:
    question = input("Oh no, please try again. ")
    print (question)
print("Congrtulations! You were correct, it was 7!")