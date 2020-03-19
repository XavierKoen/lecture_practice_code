"""Program enables the user to enter sentences, which it changes it into 'sarcastic form'.
    Some fails safes in place.
"""

text = str(input("Enter desired sentence: "))
IN_FILE = open("writing.txt", "r")
OUT_FILE = open("sarcastic_writing.txt", "w")

# number_characters = len(text)
# sarcastic_text = ''
i = 1

while not IN_FILE.read(i).isupper() or IN_FILE.read(i).islower:
    i = i + 1
    print(IN_FILE.read(i), file=OUT_FILE)
IN_FILE.read(i).lower()

for char in IN_FILE:
    if IN_FILE.read(i).islower():
       print(IN_FILE.read(i).is)
    small = text[i - 1].lower()
    sarcastic_text = sarcastic_text + small
    if i >= number_characters:
        break
    big = text[i].upper()
    sarcastic_text = sarcastic_text + big
print(sarcastic_text)
