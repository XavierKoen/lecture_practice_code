"""
Rewrite name input by user without vowels.
"""
name = input("Please enter name: ")

new_name = [c for c in name if c not in "AaEeIiOoUu"]
print("".join(new_name))
