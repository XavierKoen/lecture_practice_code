
phone_number = str(input("Please enter phone number: "))
print(phone_number)
if phone_number.startswith("07"):
    print("Is a QLD region phone number.")
else:
    print("Is not a QLD region phone number.")
