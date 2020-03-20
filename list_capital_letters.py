"""
List all capital letters found in name input by user.
"""
name = input("Please enter name: ")

capitals = [c for c in name if c.isupper()]
print("The capital letters in {} are: {}".format(name, capitals))
